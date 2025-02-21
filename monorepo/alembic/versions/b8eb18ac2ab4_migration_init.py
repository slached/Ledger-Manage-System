"""migration init

Revision ID: b8eb18ac2ab4
Revises: 
Create Date: 2025-02-22 00:33:54.155403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8eb18ac2ab4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ledgers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operation', sa.Enum('DAILY_REWARD', 'SIGNUP_CREDIT', 'CREDIT_SPEND', 'CREDIT_ADD', 'CONTENT_CREATION', 'CONTENT_ACCESS', name='ledgeroperation'), nullable=False),
    sa.Column('amount', sa.Boolean(), nullable=False),
    sa.Column('nonce', sa.String(), nullable=False),
    sa.Column('owner_id', sa.String(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ledgers_id'), 'ledgers', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ledgers_id'), table_name='ledgers')
    op.drop_table('ledgers')
    # ### end Alembic commands ###
