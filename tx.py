import requests

print('--Registration--')
name = input('Name: ')
password = input('Password: ')

while True:
    text = input()
    message = {'name': name, 'password': password, 'text': text}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
