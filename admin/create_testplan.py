import MySQLdb
import os
import sys
from sql_operations.sql import Sql
from prettytable import PrettyTable

class Create_plan:


    def __init__(self):

        self.db = Sql()


    def update_test_plan_path(self):
        print "Enter the Upcoming details carefully:"
        raw_input("Press Enter to continue...")
        test_plan_name = raw_input("Test Plan name: ")
        test_plan_path = raw_input("Test_plan_script_path: ")
        print "Now Updating ..."
        insert_test_plan_query = "insert into testplans(name,path) values ('{0}','{1}')".format(test_plan_name,test_plan_path)
        self.db.query(insert_test_plan_query)

    def show_test_plan_path_table(self):
        select_test_plan_query = "select * from testplans"
        fields = self.db.query(select_test_plan_query)
        table = PrettyTable()
        table.field_names = ["Index", "Test Plan Name", "Path"]
        for field in fields:
            table.add_row([field[0], field[1], field[2]])
        print table



create_test_plan_obj = Create_plan()
# create_test_plan_obj.update_test_plan_path()
create_test_plan_obj.show_test_plan_path_table()