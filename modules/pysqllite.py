"""
Simple python class to interact with SQLlite
"""
import sqlite3


class PySQLLite(object):

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def execute(self, statement):
        try:
            result = self.cursor.execute(statement)
            self.conn.commit()

        except Exception as e:
            raise(e)

        return result

    def fetchall(self):
        return self.cursor.fetchall()

    def exit(self):
        self.conn.commit()
        self.conn.close()
