"""All tables created

Revision ID: 473d4c9d812b
Revises: 
Create Date: 2018-12-08 19:15:36.261475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '473d4c9d812b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('favourite_color', sa.String(), nullable=False),
    sa.Column('favourite_food', sa.String(), nullable=False),
    sa.Column('favourite_song', sa.String(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('friend',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('favourite_color', sa.String(), nullable=True),
    sa.Column('favourite_food', sa.String(), nullable=True),
    sa.Column('favourite_song', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('secret',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('secret_key', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('secret_key'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('secret_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('secret')
    op.drop_table('friend')
    op.drop_table('user')
    # ### end Alembic commands ###
