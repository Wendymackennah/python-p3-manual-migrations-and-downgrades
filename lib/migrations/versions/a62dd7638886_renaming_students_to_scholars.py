"""Renaming students to scholars

Revision ID: a62dd7638886
Revises: 791279dd0760
Create Date: 2024-03-20 14:17:49.748598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a62dd7638886'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')

