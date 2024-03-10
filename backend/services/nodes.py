import csv
from typing import Type, Union

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from models.price import Price
from models.category import Category
from models.location import Location
from services.categories import get_categories
from services.locations import get_locations


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
        for row in csv.reader(await file.read())
    ]

    keys = ('id', 'name', 'parent_id')
    new_data = {
        row[0]: {key: val for key, val in zip(keys, row)}
        for row in new_data
    }

    for obj in new_data:
        obj['key'] = old_data.get(obj['parent_id'], None) or new_data.get(obj['parent_id'], {}).get('key')
        if obj['key'] is None:
            raise ValueError('Invalid data was passed')
        obj['key'] = f'{obj["key"]}-{obj["id"]}'

    await session.execute(insert(model).values(new_data).on_conflict_do_nothing())
    await session.commit()


async def add_prices(session: AsyncSession, file: UploadFile, model: type):
    if model is not Price:
        raise ValueError("Invalid 'model' passed")

    data = [
        [col if col else None for col in row]
        for row in csv.reader(await file.read())
    ]

    await session.execute(insert(model).values(data))
    await session.commit()
