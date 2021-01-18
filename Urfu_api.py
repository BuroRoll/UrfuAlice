from bs4 import BeautifulSoup
import json
from data import *
import requests


def authorization(login, password):
    response = requests.post(
        'https://sts.urfu.ru/adfs/OAuth2/authorize?resource=https%3A%2F%2Fistudent.urfu.ru&type=web_server&client_id'
        '=https%3A%2F%2Fistudent.urfu.ru&redirect_uri=https%3A%2F%2Fistudent.urfu.ru%3Fauth&response_type=code&scope=',
        data={'UserName': login,
              'Password': password,
              'AuthMethod': 'FormsAuthentication'})
    return response.cookies


def get_current_schedule(cookies, time):
    schedule = requests.post('https://istudent.urfu.ru/itribe/schedule_its/?access-token=',
                             data={'schedule_its[start_date]': time},
                             cookies=cookies)
    print(schedule.text)
    result = welcome_from_dict(json.loads(schedule.text))
    data = []
    for days in result.schedule.values():
        if days.event_date < time <= days.event_date + 86399:
            for i in days.events.values():
                data.append(i.discipline)
        break
    print(data)
    return data


def get_current_brs(cookies):
    brs_data = requests.post('https://istudent.urfu.ru/s/http-urfu-ru-ru-students-study-brs/',
                             cookies=cookies)
    soup = BeautifulSoup(brs_data.text, 'html.parser')
    data = []
    brs = {}
    for i in soup.find_all('td')[3:]:
        data.append(i.text)
    for i, j in enumerate(data):
        if i % 3 == 0:
            brs[j] = data[i + 1]
    return brs
