import csv
from typing import Type, Union

from fastapi import UploadFile
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from misc.chunk_generator import make_chunks
from models import Matrix
from models.price import Price
from models.category import Category
from models.location import Location
from services.categories import get_categories
from services.locations import get_locations


def convector(data: bytes, separator=';'):
    return [
        [int(col) if col.isdigit() else col for col in row.replace('"', '').split(separator)]
        for row in data.decode().strip().split('\n')
    ]


async def delete_table(session: AsyncSession, model: Type[Union[Category, Matrix, Location, Price]]):
    await session.execute(delete(model))
    await session.commit()


async def add_nodes_pack(session: AsyncSession, file: UploadFile, model: Type[Union[Location, Category]]):
    if model is not Category and model is not Location:
        raise ValueError("Invalid 'model' passed")

    context = {
        Location: get_locations,
        Category: get_categories,
    }

    old_data = {obj.id: obj for obj in await context[model](session)}

    new_data = [
        [col if col else None for col in row]
        for row in convector(await file.read())
    ]

    keys = ('id', 'name', 'parent_id')
    new_data = {
        row[0]: {key: val for key, val in zip(keys, row)}
        for row in new_data
    }

    for k, obj in new_data.items():
        obj['key'] = old_data.get(obj['parent_id'], None) or new_data.get(obj['parent_id'], {}).get('key')
        if obj['key'] is None and obj['parent_id'] is not None:
            raise ValueError('Invalid data was passed')
        obj['key'] = f'{obj["id"]}-{obj["key"]}' if obj['parent_id'] is not None else str(obj['id'])

    for chunk in make_chunks(list(new_data.values())):
        await session.execute(insert(model).values(chunk).on_conflict_do_nothing())

    await session.commit()


async def add_prices(session: AsyncSession, file: UploadFile, model: type, matrix: Matrix):
    if model is not Price:
        raise ValueError("Invalid 'model' passed")

    data = [
        {
            'price': int(row[2]),
            'matrix_id': matrix.id,
            'location_id': int(row[1]),
            'category_id': int(row[0])
        }
        for row in convector(await file.read())
    ]

    for chunk in make_chunks(data):
        await session.execute(insert(model).values(chunk).on_conflict_do_nothing())

    await session.commit()
