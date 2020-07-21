# pyuic5 messenger.ui -o clientui.py

import sys
import requests
import time
from PyQt5 import QtWidgets, QtCore
from clientui import Ui_MainWindow
from datetime import datetime
from configparser import ConfigParser


class MessengerWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.pB_send.pressed.connect(self.send_message)

        self.after = time.time() - 24 * 60 * 60

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def set_status(self, text):
        self.statusbar.showMessage(text)
        self.statusbar.repaint()

    def add_text(self, text):
        self.tB_chat.append(text)
        self.tB_chat.repaint()

    def format_message(self, message):
        name = message['name']
        text = message['text']
        dt = datetime.fromtimestamp(message['time'])
        dt_format = dt.strftime('%d/%m/%Y %H:%M:%S')
        return f'{dt_format}\n{name}: {text}\n'

    def update_messages(self):
        try:
            response = requests.get(f'{self.url}/messages', params={'after': self.after})
        except:
            return

        messages = response.json()['messages']
        for message in messages:
            self.add_text(self.format_message(message))
            self.after = message['time']

    def send_message(self):
        name = self.lE_login.text()
        password = self.lE_password.text()
        text = self.tE_message.toPlainText()

        if not name or not password or not text:
            self.set_status('Fill in empty fields')
            return

        message = {'name': name, 'password': password, 'text': text}

        try:
            response = requests.post(f'{self.url}/send', json=message)
        except:
            self.set_status('Server unavailable')
            return

        if response.status_code == 200:
            self.tE_message.clear()
            self.tE_message.repaint()
            self.set_status('')
        elif response.status_code == 401:
            self.set_status('Wrong name/password')
        else:
            self.set_status('Unknown error')


config = ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MessengerWindow(config['URLs']['server_url'])
    window.show()
    sys.exit(app.exec_())
