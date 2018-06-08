import sqlite3
import os


class BaseDB:
    __db_path = './test.db'

    def __init__(self):
        db_exists = os.path.exists(self.__db_path)

        self.conn = self.__conn()
        self.cursor = self.conn.cursor()

        if not db_exists:
            self.__create_table(self.cursor)

    def __conn(self):
        return sqlite3.connect(self.__db_path)


    def close(self):
        self.conn.close()

    def __create_table(self, cursor):
        cursor.execute('''
            CREATE TABLE NAV
            (ITEM  TEXT  NOT  NULL);
            ''')
        self.conn.commit()
