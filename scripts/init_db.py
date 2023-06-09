from utils import create_app
from models import Pessoa
from models import db

def insert_dummy_data():
    """Insert dummy data"""

    app = create_app(db)
    with app.app_context():

        pessoa_obj: Pessoa = Pessoa(
            nome="Yorran Rigatti",
            cpf="04341594099",
            data_nascimento="2000-07-17",
        )
        pessoa_obj.save()
