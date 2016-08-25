import MySQLdb
import os
import sys

class Sql:
    host = 'localhost'
    user = 'root'
    password = 'nvidia123'
    db = 'nvidia'
    insert_state = ''
    update_sql = ""

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print "Inserted"
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()