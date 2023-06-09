"""Initial migration.

Revision ID: 77123e0e8e19
Revises: 
Create Date: 2023-03-09 03:58:08.023874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "77123e0e8e19"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "conta",
        sa.Column("idConta", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("idPessoa", sa.Integer(), nullable=True),
        sa.Column("saldo", sa.Numeric(16, 2), nullable=True),
        sa.Column("limiteSaqueDiario", sa.Numeric(16, 2), nullable=True),
        sa.Column("flagAtivo", sa.Boolean(), nullable=True),
        sa.Column("tipoConta", sa.Integer(), nullable=True),
        sa.Column("dataCriacao", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("idConta"),
    )
    op.create_table(
        "pessoa",
        sa.Column("idPessoa", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.Text(), nullable=True),
        sa.Column("cpf", sa.Text(), nullable=True),
        sa.Column("dataNascimento", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("idPessoa"),
    )
    op.create_table(
        "transacao",
        sa.Column("idTransacao", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("idConta", sa.Integer(), nullable=True),
        sa.Column("valor", sa.Numeric(16, 2), nullable=True),
        sa.Column("dataTransacao", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("idTransacao"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transacao")
    op.drop_table("pessoa")
    op.drop_table("conta")
    # ### end Alembic commands ###
