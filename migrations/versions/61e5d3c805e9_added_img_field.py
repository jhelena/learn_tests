"""added img field

Revision ID: 61e5d3c805e9
Revises: c83e8637ecc6
Create Date: 2019-11-02 22:55:31.143014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61e5d3c805e9'
down_revision = 'c83e8637ecc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('img_name', sa.String(255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'img_name')
    # ### end Alembic commands ###