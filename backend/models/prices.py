from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.engine import Base
from models.matrices import Matrices
from models.locations import Locations
from models.categories import Categories


class Prices(Base):
    __tablename__ = "prices"

    price: Mapped[int] = mapped_column()

    matrix_id: Mapped[int] = mapped_column(ForeignKey("matrices.id"), primary_key=True)
    matrix: Mapped[Matrices] = relationship(back_populates="prices")

    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), primary_key=True)
    location: Mapped[Locations] = relationship(back_populates="prices")

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)
    category: Mapped[Categories] = relationship(back_populates="prices")


