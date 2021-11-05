"""empty message

Revision ID: 9ced4a7198a6
Revises: 4dbc044a5f1a
Create Date: 2021-10-27 23:53:29.515264

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9ced4a7198a6'
down_revision = '4dbc044a5f1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('MenuPosition', sa.Column('images', sa.String(), nullable=True))
    op.drop_column('MenuPosition', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('MenuPosition', sa.Column('image', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.drop_column('MenuPosition', 'images')
    # ### end Alembic commands ###
