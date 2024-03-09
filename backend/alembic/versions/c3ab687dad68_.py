"""empty message

Revision ID: c3ab687dad68
Revises: 
Create Date: 2024-03-09 19:20:20.696270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3ab687dad68'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('parent_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('parent_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matrices',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('segment_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prices',
    sa.Column('matrix_id', sa.INTEGER(), nullable=False),
    sa.Column('location_id', sa.INTEGER(), nullable=False),
    sa.Column('microcategory_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['matrix_id'], ['matrices.id'], ),
    sa.ForeignKeyConstraint(['microcategory_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('matrix_id', 'location_id', 'microcategory_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prices')
    op.drop_table('matrices')
    op.drop_table('locations')
    op.drop_table('categories')
    # ### end Alembic commands ###
