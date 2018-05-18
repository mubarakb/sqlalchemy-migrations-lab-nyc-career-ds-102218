"""create_ski_bums

Revision ID: 6ca02214fcb1
Revises: 878b88d31e6d
Create Date: 2018-05-18 16:37:43.356560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ca02214fcb1'
down_revision = '878b88d31e6d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('ski_bums',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('acl_surgery_yet', sa.Boolean),
        sa.Column('vertical_skied', sa.BigInteger),
        sa.Column('fave_run_description', sa.Text),
        sa.Column('days_skied_to_not_skied_ratio', sa.Float)
    )


def downgrade():
    op.drop_table('ski_bums')
