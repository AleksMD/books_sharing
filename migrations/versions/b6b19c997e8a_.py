"""empty message

Revision ID: b6b19c997e8a
Revises: 34d987a5b4f7
Create Date: 2019-12-09 19:09:48.162179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6b19c997e8a'
down_revision = '34d987a5b4f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('owner', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'books', 'users', ['owner'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'owner')
    # ### end Alembic commands ###
