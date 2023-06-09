from .base_mixin import BaseModelMixin, db


class Transacao(db.Model, BaseModelMixin):
    """Transacao Model class"""

    id_transacao = db.Column(
        "idTransacao", db.Integer, primary_key=True, autoincrement=True
    )
    id_conta = db.Column("idConta", db.Integer)
    valor = db.Column("valor", db.Numeric(16,2))
    data_transacao = db.Column("dataTransacao", db.Date)
