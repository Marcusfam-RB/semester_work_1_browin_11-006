"""empty message

Revision ID: 579a983259b2
Revises: 8d4eb5b5efcf
Create Date: 2021-10-25 21:58:25.838142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579a983259b2'
down_revision = '8d4eb5b5efcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('MenuPosition', sa.Column('type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('MenuPosition', 'type')
    # ### end Alembic commands ###
