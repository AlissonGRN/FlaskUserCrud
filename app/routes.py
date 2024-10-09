from flask import Flask
from app.controllers import user_controller

# Função para inicializar as rotas da aplicação
def init_routes(app: Flask):
    # Rota para listar e criar usuários
    app.add_url_rule('/users', view_func=user_controller.get_users, methods=['GET'])
    app.add_url_rule('/users', view_func=user_controller.create_user, methods=['POST'])

    # Rota para obter, atualizar e deletar um usuário específico
    app.add_url_rule('/users/<int:user_id>', view_func=user_controller.get_user, methods=['GET'])
    app.add_url_rule('/users/<int:user_id>', view_func=user_controller.update_user, methods=['PUT'])
    app.add_url_rule('/users/<int:user_id>', view_func=user_controller.delete_user, methods=['DELETE'])
