from flask import Flask, request, abort
from datetime import datetime
import time
import requests
import random
import re

servername = 'Chibis'
is_bot_working = False

#Добавить получение данных из БД
messages = [{
    'name': f'{servername} server',
    'text': f'Server started. To see bot commands type /commands',
    'time': time.time()
}]

users = {}

app = Flask(__name__)

@app.route('/')
def hello_view():
    return f'Welcome to {servername} server.' \
           f' To check status click: <a href = "/status">Status </a>'


@app.route('/status')
def status_view():
    return {
        'status': True,
        'messenger': f'{servername} messenger',
        'time 1': datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f'),
        'total_users': len(users),
        'total_messages': len(messages)
    }
def look_for_weather():
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    city_id = 524894
    appid = '???'

    params = {
        'id': city_id,
        'appid': appid,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        w_response = requests.get(api_url, params=params)
        w_data = w_response.json()
        temperature = w_data['main']['temp']
        conditions = w_data['weather'][0]['description']
        weather = f'{temperature}, {conditions}'

        return weather
    except:
        return 'Не могу найти('

def bot_check(input_text):
    global is_bot_working
    output_text = ''

    if input_text == '/commands':
        output_text = '/start - start bot \n' \
                      '/stop - stop bot'
    if is_bot_working:
        if input_text == '/stop':
            is_bot_working = False
            output_text = random.choice(['До скорых встреч', 'Пока', 'Все, я спать',
                                         'Бот выключен', 'Гудбай'])
        elif re.match('(?i)чиб[ а]|чибис|чибул[ья]', input_text):
            if re.search('(?i)как', input_text) and re.search('(?i)дела|жизнь|ты', input_text):
                output_text = random.choice(['Все пучком', 'Отлично!', 'Супер'])
            elif re.search('(?i)погод[аыу]', input_text):
                output_text = look_for_weather()

    if not is_bot_working:
        if input_text == '/start':
            is_bot_working = True
            output_text = random.choice(['Чем могу быть полезен?', 'Бот активирован.',
                                         'Всем привет!', 'Как дела?', 'А вот и я!']) + ' Зови меня Чиба'

    return output_text


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

    bot_reply = bot_check(text)
    if bot_reply != '':
        messages.append({'name': f'{servername} bot', 'text': bot_reply, 'time': time.time()})


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
