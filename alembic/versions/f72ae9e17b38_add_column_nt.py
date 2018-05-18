"""add_column_nt

Revision ID: f72ae9e17b38
Revises:
Create Date: 2018-05-18 16:31:51.910961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f72ae9e17b38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('ninjaturtles', sa.Column('headband_color', sa.String()))


def downgrade():
    op.drop_column('ninjaturtles', 'headband_color')
