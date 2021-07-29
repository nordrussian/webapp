"""empty message

Revision ID: 29b845804645
Revises: 5550830cbc9f
Create Date: 2021-06-09 01:13:37.466334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29b845804645'
down_revision = '5550830cbc9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lecturer', sa.Column('tel', sa.Text(), nullable=True))
    op.add_column('lecturer', sa.Column('email', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lecturer', 'email')
    op.drop_column('lecturer', 'tel')
    # ### end Alembic commands ###
