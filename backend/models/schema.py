from sqlalchemy import String, INT, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Locations(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(INT, primary_key=True)
    key: Mapped[str] = mapped_column(String())
    name: Mapped[str] = mapped_column(String())

    parent_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(INT, primary_key=True)
    key: Mapped[str] = mapped_column(String())
    name: Mapped[str] = mapped_column(String())

    parent_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))


class Prices(Base):
    __tablename__ = "prices"

    matrix_id: Mapped[int] = mapped_column(ForeignKey("matrices.id"), primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), primary_key=True)
    microcategory_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)


class Matrices(Base):
    __tablename__ = "matrices"

    id: Mapped[int] = mapped_column(INT, primary_key=True)
    name: Mapped[str] = mapped_column(String())
    segment_id: Mapped[int] = mapped_column(INT, nullable=True)

