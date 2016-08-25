import os
import MySQLdb
from extract_data_from_csv_to_database import Database


class nvtest:

    host = 'localhost'
    user = 'root'
    password = 'nvidia123'
    db = 'nvidia'
    insert_state = ''
    update_sql = ""


    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()





print ":::: Welcome to NVTEST ::::"

print "Authorize yourself to system to continue:"

print

