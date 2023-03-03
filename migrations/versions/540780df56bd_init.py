"""Init

Revision ID: 540780df56bd
Revises: 3cf6a066cf7b
Create Date: 2023-03-03 10:08:55.575191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540780df56bd'
down_revision = '3cf6a066cf7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###
