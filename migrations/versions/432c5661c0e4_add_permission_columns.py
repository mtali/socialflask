"""Add permission columns

Revision ID: 432c5661c0e4
Revises: c073e15c0ee0
Create Date: 2019-03-31 11:02:51.215661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432c5661c0e4'
down_revision = 'c073e15c0ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
