from app import db
from datetime import datetime

class User(db.Model): # TODO Atualizar User para conter atributos de senha e role 

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # Chave primária
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email (único)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Data de criação
    

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    # TODO Adcionar função para gerar e armazenar o hash da senha e verificar a senha 
