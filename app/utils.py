import psycopg2
from psycopg2.extras import RealDictCursor
import time


def connect():
    while True:
        print('Conecting to the Database..... Please wait')
        time.sleep(3)
        try:
            connection = psycopg2.connect(host='127.0.0.1', database = "fastApi_db", user='postgres', password='root', cursor_factory=RealDictCursor)
            cursor = connection.cursor()
            print('Successfully Connected to the database')
            return cursor
            
        except Exception as e:
            print("Error trying to connect to the database....")
            print('ErroR: ', e)
