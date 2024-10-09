import os

class Config:
    # URL de conexão ao banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://alisson:alisson123@localhost/minha_api_db'
    
    # Desabilitamos o track de modificações para evitar overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False
