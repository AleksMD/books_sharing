"""empty message

Revision ID: 20114990000d
Revises: b6b19c997e8a
Create Date: 2019-12-09 20:14:09.895135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20114990000d'
down_revision = 'b6b19c997e8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('library',
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='library_book_id_fkey'),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='library_owner_id_fkey')
    )
    # ### end Alembic commands ###
