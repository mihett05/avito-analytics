from datetime import datetime

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from models.engine import Base


class StorageLogs(Base):
    __tablename__ = "storage_logs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    baseline: Mapped[int] = mapped_column()
    discounts: Mapped[ARRAY] = mapped_column()
    happened_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
