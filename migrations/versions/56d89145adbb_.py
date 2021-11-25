"""empty message

Revision ID: 56d89145adbb
Revises: 7b4e00130929
Create Date: 2021-10-13 16:52:58.961413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "56d89145adbb"
down_revision = "7b4e00130929"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("name", sa.String(), nullable=True))
        batch_op.drop_column("email")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "email", sa.VARCHAR(), autoincrement=False, nullable=True
            )
        )
        batch_op.drop_column("name")

    # ### end Alembic commands ###