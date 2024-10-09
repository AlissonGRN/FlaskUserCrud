import os

class Config:
    # URL de conexão ao banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://alisson:alisson123@localhost/minha_api_db')
    
    # Desabilitamos o track de modificações para evitar overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False
