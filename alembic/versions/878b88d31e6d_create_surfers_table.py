"""create_surfers_table

Revision ID: 878b88d31e6d
Revises: f72ae9e17b38
Create Date: 2018-05-18 16:33:57.875104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '878b88d31e6d'
down_revision = 'f72ae9e17b38'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'surf_pirates',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('largest_wave_surfed', sa.Integer),
        sa.Column('seen_great_white', sa.Boolean),
        sa.Column('date_started_surfing', sa.DateTime)
    )


def downgrade():
    op.drop_table('surf_pirates')
