"""empty message

Revision ID: 12c67caedc72
Revises: f48a48c4d693
Create Date: 2019-12-09 14:41:29.853873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c67caedc72'
down_revision = 'f48a48c4d693'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('hidden', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'hidden')
    # ### end Alembic commands ###
