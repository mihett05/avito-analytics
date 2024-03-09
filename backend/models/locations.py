from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.engine import Base


class Locations(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()

    parent_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
