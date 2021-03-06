"""empty message

Revision ID: 801a4e6b3262
Revises: 1ea7100d95d0
Create Date: 2018-04-24 16:10:41.783246

"""

# revision identifiers, used by Alembic.
revision = '801a4e6b3262'
down_revision = '1ea7100d95d0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('irma_fileExt', sa.Column('depth', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('irma_fileExt', 'depth')
    # ### end Alembic commands ###
