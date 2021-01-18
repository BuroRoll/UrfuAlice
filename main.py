from flask import Flask
from flask import request
from dbHelper import *
from Urfu_api import *
import time

from strings import *

app = Flask(name)
schedules_commands = ['скажи расписание', 'сегодняшнее расписание']
schedules_commands_tomorrow = ['скажи расписание на завтра', 'завтрашнее расписание', 'расписание на завтра']
brs_commands = ['какие у меня баллы', 'сколько у меня баллов', 'что у меня в брс', 'брс']


@app.route('/Alice', methods=['POST'])
def main():
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res, req):
    command = req['request']['command']
    user_id = req['session']['user']['user_id']
    if command == 'авторизация':
        authorization_answer(res)
    elif command.startswith('login'):
        login = req['request']['original_utterance'][6:]
        add_user(user_id, login)
        res['response']['text'] = login_saves
    elif command.startswith('password'):
        password = req['request']['original_utterance'][9:]
        update_user_password(user_id, password)
        res['response']['text'] = password_saved
    elif command in schedules_commands:
        schedule_answer(res, user_id, time.time())
    elif command in schedules_commands_tomorrow:
        schedule_answer(res, user_id, time.time() + 86399)
    elif command == 'спасибо':
        res['response']['text'] = have_a_good_day
        res['response']['end_session'] = True
    elif command in brs_commands:
        brs_answer(res, user_id)
    else:
        if check_user(user_id):
            res['response']['text'] = info
        else:
            inf = info + ', но для начала необходимо авторизоваться, чтобы узнать, как это сделать скажи "авторизация"'
            res['response']['text'] = inf


def authorization_answer(res):
    res['response']['text'] = autorization_answer


def schedule_answer(res, user_id, data):
    login, password = get_user(user_id)
    cookies = authorization(login, password)
    schedule = get_current_schedule(cookies, data)
    if time.time() - data > 0:
        answer = 'Сегодня у тебя '
    else:
        answer = 'Завтра у тебя '
    if len(schedule) == 0:
        answer = answer + ' нет пар'
    else:
        answer = answer + ', '.join(schedule)
    res['response']['text'] = answer


def brs_answer(res, user_id):
    login, password = get_user(user_id)
    cookies = authorization(login, password)
    brs = get_current_brs(cookies)
    if brs is not None:
        str = 'Твои баллы: \n'
        for name in brs:
            if float(brs[name]) > 0:
                r = f'{name} {brs[name]}, \n'
                str = str + r
        res['response']['text'] = str
    else:
        res['response']['text'] = 'В БРС пусто'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
