"""empty message

Revision ID: c1169c43c2f7
Revises: 33552ac90c88
Create Date: 2024-07-12 12:10:27.242076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1169c43c2f7'
down_revision = '33552ac90c88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name=op.f('fk_books_author_id_authors')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
