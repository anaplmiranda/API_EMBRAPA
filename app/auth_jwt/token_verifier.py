from functools import wraps
from flask import jsonify, request
import jwt
from .token_handler import token_creator

def token_verify(function: callable) -> callable:

    @wraps(function)
    def decorated(*arg, **kwargs):
            raw_token = request.headers.get('Authorization')
            uid = request.headers.get('uid')

            if not raw_token or not uid:
                return jsonify({
                    'error': 'Bad Request: Authorization header ou uid ausente.'
                }),400
            
            if not raw_token.startswith("Bearer "):
                return jsonify({
                    'error': 'Formato do token inválido. O token deve estar no formato "Bearer <token>".'
                }), 400
    
            try:
                token = raw_token.split()[1]
                token_information = jwt.decode(token, key='1234', algorithms=["HS256"])

                if not isinstance(token_information, dict) or 'uid' not in token_information:
                    return jsonify({'error': 'Token inválido: uid ausente no payload'}), 401
                
                token_uid = token_information['uid']

            except jwt.InvalidSignatureError:
                return jsonify({
                    'error': 'Token Invalido'
                }),401
            except jwt.ExpiredSignatureError:    
                return jsonify({
                    'error': 'Token Expirado'
                }),401
            except KeyError as e:
                return jsonify({
                    'error': 'Token Invalido'
                }),401
            except Exception as e:
                return jsonify({
                    'error': f'Erro ao processar o token: {str(e)}'
                }), 500
            
            if uid and token_uid and (int(token_uid) != int(uid)):
                return jsonify({
                    'error': 'user não permitido'
                }),401
            
            try:
                next_token = token_creator.refresh(token)
            except AttributeError:
                return jsonify({
                    'error': 'Função refresh não encontrada em token_creator'
                }), 500

            return function(next_token, *arg, **kwargs)
    
    return decorated