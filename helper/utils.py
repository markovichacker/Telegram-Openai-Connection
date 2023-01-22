import json
from flask import request


from outside_apis.openai_api import text_complition

def process_request(request: request) -> dict:
    '''
    Process the incoming data of the Telegram request

    Parameters:
        - request(falsk.request)

    Returns:
        - dict of these key and value 
        {
            'is_text': is_text,
            'is_chat_deleted': is_chat_deleted,
            'sender_id': sender_id,
            'message': message,
            'secret_token': secret_token,
            'first_name': first_name
        }
    '''
    
    body = request.get_json()
    print(body)
    headers = request.headers
    secret_token = headers['X-Telegram-Bot-Api-Secret-Token']

    message = ''
    is_bot = True
    is_text = False
    first_name = ''
    sender_id = None


    if 'message' in body.keys():
        sender_id = body['message']['from']['id']
        first_name = body['message']['from']['first_name']
        is_bot = body['message']['from']['is_bot']

        if 'text' in body['message'].keys():
            message += body['message']['text']
            is_text = True

    return {
        'is_text': is_text,
        'sender_id': sender_id,
        'message': message,
        'secret_token': secret_token,
        'first_name': first_name,
        'is_bot': is_bot
    }

def generate_response(message: str) -> str:
    '''
    Process the incoming message for different command and generate a response string

    Parameters:
        - message(str): incoming message from Telegram

    Returns:
        - str: formated response for the command
    '''
    if message == '/seguime':
        return 'https://instagram.com/vigmarco'
    elif message == '/ayuda':
        return 'Alfa Bot puede responder cualquier pregunta del universo'
    elif message == '/stickers':
        return 'https://t.me/addstickers/madmensamid ** https://t.me/addstickers/lucreciamstickers ** https://t.me/addstickers/mansonstickers ** https://t.me/addstickers/bizarristickers'
    elif message == 'Yo voy en trenes':
        return '...no tengo donde ir'
    elif message == 'Proceda':
        return '> Modo Maslatón Activado <'
    elif message == 'Hola Alfa':
        return 'Los likes de tik tok no son lealtad, son likes. Nada más.'
    elif message == 'Tengo sueño':
        return 'Retirate si no querés morir.'
    elif message == 'Votos':
        return 'Y mi segundo voto es para Luciana.'
    elif message == '/start':
        return 'No tengo necesidad de agarrar una pala porque soy inteligente, Holder.'
    else:
        result = text_complition(message)
        if result['status'] == 1:
            return result['response'].strip()
        else:
            return 'Ahora no, estoy descansando.'
            
