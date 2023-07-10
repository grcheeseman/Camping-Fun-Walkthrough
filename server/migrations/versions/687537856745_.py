"""empty message

Revision ID: 687537856745
Revises: 1e7a63eb1943
Create Date: 2023-07-10 14:42:06.182780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '687537856745'
down_revision = '1e7a63eb1943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###