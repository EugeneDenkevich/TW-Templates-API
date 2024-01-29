"""fix table names

Revision ID: e7b19542e7e1
Revises: 62373f06f227
Create Date: 2024-01-29 17:39:25.794775

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e7b19542e7e1"
down_revision: Union[str, None] = "62373f06f227"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "kitchen",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("display", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.drop_table("menu")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "menu",
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("display", sa.BOOLEAN(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.drop_table("kitchen")
    # ### end Alembic commands ###
