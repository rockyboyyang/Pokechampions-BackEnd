"""create users and trainers tables

Revision ID: c553689aee65
Revises: 
Create Date: 2020-08-13 11:33:29.355531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c553689aee65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trainers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('slot_1', sa.String(), nullable=False),
    sa.Column('slot_2', sa.String(), nullable=False),
    sa.Column('slot_3', sa.String(), nullable=False),
    sa.Column('slot_4', sa.String(), nullable=False),
    sa.Column('slot_5', sa.String(), nullable=False),
    sa.Column('slot_6', sa.String(), nullable=False),
    sa.Column('trainerClass', sa.String(length=30), nullable=False),
    sa.Column('bio', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.Column('slot_1', sa.String(), nullable=True),
    sa.Column('slot_2', sa.String(), nullable=True),
    sa.Column('slot_3', sa.String(), nullable=True),
    sa.Column('slot_4', sa.String(), nullable=True),
    sa.Column('slot_5', sa.String(), nullable=True),
    sa.Column('slot_6', sa.String(), nullable=True),
    sa.Column('rank', sa.String(length=15), nullable=False),
    sa.Column('boulderbadge', sa.Boolean(), nullable=False),
    sa.Column('cascadebadge', sa.Boolean(), nullable=False),
    sa.Column('thunderbadge', sa.Boolean(), nullable=False),
    sa.Column('rainbowbadge', sa.Boolean(), nullable=False),
    sa.Column('soulbadge', sa.Boolean(), nullable=False),
    sa.Column('marshbadge', sa.Boolean(), nullable=False),
    sa.Column('volcanobadge', sa.Boolean(), nullable=False),
    sa.Column('earthbadge', sa.Boolean(), nullable=False),
    sa.Column('beatElite4_1', sa.Boolean(), nullable=False),
    sa.Column('beatElite4_2', sa.Boolean(), nullable=False),
    sa.Column('beatElite4_3', sa.Boolean(), nullable=False),
    sa.Column('beatElite4_4', sa.Boolean(), nullable=False),
    sa.Column('beatChampion', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('trainers')
    # ### end Alembic commands ###
