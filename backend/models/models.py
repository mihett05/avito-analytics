from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

from config import get_config

config = get_config()
database_url = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:" \
               f"{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = create_async_engine(database_url, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def init_models():
    pass


class Locations(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()

    parent_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()

    parent_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))


class Prices(Base):
    __tablename__ = "prices"

    price: Mapped[int] = mapped_column()
    matrix_id: Mapped[int] = mapped_column(ForeignKey("matrices.id"), primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), primary_key=True)
    microcategory_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)


class Matrices(Base):
    __tablename__ = "matrices"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    segment_id: Mapped[int] = mapped_column(nullable=True)
