from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)

messages = [
    {'name': 'Jack', 'time': time.time(), 'text': '123'},
    {'name': 'Jack', 'time': time.time(), 'text': '1234'}
]

users = {
    'Jack': '1234'
}


@app.route('/')
def hello_view():
    return 'Hello, World! <a href = "/status">Статус </a>'


@app.route('/status')
def status_view():
    return {
        'status': True,
        'messenger': 'PooKan Messenger',
        'time 1': datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f'),
        'total_users': len(users),
        'total_messages': len(messages)
    }


@app.route('/send', methods=['POST'])
def send_view():
    name = request.json.get('name')
    password = request.json.get('password')
    text = request.json.get('text')

    for token in [name, password, text]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)

    if name in users:
        if users[name] != password:
            abort(401)
    else:
        users[name] = password

    messages.append({'name': name, 'text': text, 'time': time.time()})

    return {'ok': True}


def filter_dicts(elements, key, min_value):
    new_elements = []

    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)

    return new_elements


@app.route('/messages')
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        abort(400)

    filtered_messages = filter_dicts(messages, key='time', min_value=after)

    return {'messages': filtered_messages}


app.run()
