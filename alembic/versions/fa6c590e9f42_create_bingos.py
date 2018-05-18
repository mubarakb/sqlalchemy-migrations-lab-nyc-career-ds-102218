"""create_bingos

Revision ID: fa6c590e9f42
Revises: 6ca02214fcb1
Create Date: 2018-05-18 16:43:49.737136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa6c590e9f42'
down_revision = '6ca02214fcb1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('bingo_players', sa.Column('id', sa.Integer, primary_key=True), sa.Column('name', sa.String()))


def downgrade():
    op.drop_table('bingo_players')
