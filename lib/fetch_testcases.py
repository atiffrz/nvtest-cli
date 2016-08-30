import MySQLdb
import os
import sys
from prettytable import PrettyTable
from sql_operations.sql import Sql

class cases:

    def __init__(self):
       self.db = Sql()

    def fetch_testplans(self,show=0):
        if show == 0:
            machine_query = "select * from testplans"
            fields = self.db.query(machine_query)
            table = PrettyTable()
            table.field_names = ["Sr No.", "Test Plan"]
            for field in fields:
                table.add_row([field[0], field[1]])
            print table

    def fetch_testcases(self,test_plan_id):
        test_query = "select short_name from testplans where testplans.index={0}".format(test_plan_id)
        fields = self.db.query(test_query)
        testplan_name = ""
        for field in fields:
            testplan_name = field[0]

        machine_query = "select * from {0}".format(testplan_name)
        fields = self.db.query(machine_query)
        table = PrettyTable()
        table.field_names = ["Template ID", "Template Name"]
        for field in fields:
            table.add_row([field[0], field[1]])
        print table

    # def scriptpath_selector(self, testplan_number):
    #     path_query = "select path from testplans where index={0}".format(testplan_number)
    #     result = self.db.query(path_query)
    #     for field in result:
    #         self._scpath = field[0]





# fetch_testcases_obj = cases()
#
# fetch_testcases_obj.fetch_testplans(0)
# fetch_testcases_obj.fetch_testcases("graphics")
