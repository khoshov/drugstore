"""init

Revision ID: 030511b1bccd
Revises: 
Create Date: 2022-11-02 23:17:11.515781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030511b1bccd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image', sa.Unicode(length=128), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('discount_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['discount_id'], ['discount.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('discount')
    # ### end Alembic commands ###