from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.engine import Base


class Matrix(Base):
    __tablename__ = "matrices"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    segment_id: Mapped[int] = mapped_column(nullable=True)

    prices = relationship("Price", back_populates="matrix")
