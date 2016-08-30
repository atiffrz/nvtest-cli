import MySQLdb
import sys
import os
from sql_operations.sql import Sql



class login:

    def __init__(self):
        self.db = Sql()



    def input_login(self):
        print "Enter the login details:"
        user_id = raw_input("UserID:")
        passwd = raw_input("Password:")


        select_query = "select * from users"
        user = self.db.query(select_query)

        for person in user:
            if user_id == person[0] and passwd == person[1]:
                return 1
            else:
                return 0






