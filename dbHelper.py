from peewee import *

db = SqliteDatabase('myDB.db')


class Data(Model):
    name = TextField()
    login = TextField()
    password = TextField()

    class Meta:
        database = db


def add_user(name, login):
    Data.create(name=name, login=login, password='')


def update_user_password(name, password):
    user = Data.select().where(Data.name == name).get()
    user.password = password
    user.save()


def get_user(name):
    login = Data.select().where(Data.name == name).get().login
    password = Data.select().where(Data.name == name).get().password
    return login, password

def check_user(name):
    if Data.select().where(Data.name == name):
        return True
    return False
