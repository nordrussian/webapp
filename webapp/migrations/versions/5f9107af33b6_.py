"""empty message

Revision ID: 5f9107af33b6
Revises: 29b845804645
Create Date: 2021-06-09 01:16:45.292078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f9107af33b6'
down_revision = '29b845804645'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lecturer', sa.Column('city', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lecturer', 'city')
    # ### end Alembic commands ###
