"""add id autoincrement to matrix

Revision ID: b71ee920c323
Revises: cdd4d0ad495d
Create Date: 2024-03-10 17:03:03.622956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b71ee920c323'
down_revision: Union[str, None] = 'cdd4d0ad495d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###