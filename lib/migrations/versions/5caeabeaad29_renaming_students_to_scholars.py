"""Renaming students to scholars

Revision ID: 5caeabeaad29
Revises: 791279dd0760
Create Date: 2023-09-06 15:14:33.009404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5caeabeaad29'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

