from flask import Blueprint, request, jsonify
from src.services.user_service import UserService
user_service = UserService('db.json')
from flask_jwt_extended import jwt_required, get_jwt_identity

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username: str = data.get('username')
    mail: str = data.get('mail')
    password: str = data.get('password')

    if not username or not mail or not password:
        return jsonify({'message': 'Se requieren los campos username, mail y password'}), 400
    
    if not user_service.register_user(username, mail, password):
        return jsonify({'message': 'Nombre de usuario o correo ya existen'}), 400

    return jsonify({'message': 'Usuario registrado con éxito'}), 201


@user_routes.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username: str = data.get('username')
    password: str = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Se requieren los campos username y password para poder loguearte.'}), 400
    
    token = user_service.login_user(username, password)
    if not token:
        return jsonify({'message': 'Nombre de usuario o contraseña incorrecta.'}), 400

    return jsonify({'token': token}), 201


@user_routes.route('/puedopasar', methods=['GET'])
@jwt_required()
def puede_pasar():
    current_user = get_jwt_identity()
    user = user_service.find_user_by_id(current_user)
    user_param = request.args.get('user')
    
    if user.username == user_param:
        return jsonify({'puede_pasar': True, 'user': user.username})
    else:
        return jsonify({'puede_pasar': False})
    

@user_routes.route('/users', methods=['GET'])
@jwt_required()
def get_all_usernames():
    users = user_service.load_users()
    usernames = [user.username for user in users]
    return jsonify({'usernames': usernames})