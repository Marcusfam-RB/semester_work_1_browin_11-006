"""empty message

Revision ID: b249d38265bf
Revises: 3f811a23e23b
Create Date: 2021-11-04 15:56:57.841798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b249d38265bf'
down_revision = '3f811a23e23b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Orders')
    op.drop_table('OrdersPositions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('OrdersPositions',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"OrdersPositions_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('position_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['Orders.id'], name='OrdersPositions_order_id_fkey'),
    sa.ForeignKeyConstraint(['position_id'], ['MenuPosition.id'], name='OrdersPositions_position_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='OrdersPositions_pkey')
    )
    op.create_table('Orders',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Orders_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_done', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='Orders_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Orders_pkey')
    )
    # ### end Alembic commands ###
