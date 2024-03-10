import csv
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from models.category import Category
from models.location import Location


async def read_and_add_nodes(session: AsyncSession, file: UploadFile, model: type):
    if model is not Category and model is not Location:
        raise ValueError("Invalid 'model' passed")
    data = [
        [col if col else None for col in row] for row in csv.reader(await file.read())
    ]
    await session.execute(insert(model).values(data))
    await session.commit()
