"""re-Fixed all cascade delete in all models

Revision ID: 9d19192b708b
Revises: 7a3b1e3d3bd2
Create Date: 2021-07-19 10:41:56.733940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d19192b708b'
down_revision = '7a3b1e3d3bd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'colunateste')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('colunateste', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
