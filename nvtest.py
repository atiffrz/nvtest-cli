import os
import MySQLdb
from extract_data_from_csv_to_database import Database
from lib.userlogin import login
from lib.fetch_machines import machines
from lib.fetch_testcases import cases
import time
from lib.execute_test import Execute


class nvtest:

    def __init__(self):
        self.login = login()
        self.machine = machines()
        self.test = cases()
        self.execute = Execute()

    def main(self):
        if self.login.input_login():
            print "Hola !! You are authenticated"
            info = raw_input("Do ypu want short info of machines present in farm (y/n): ")
            if info == "n" or info == "N":
                self.machine.fetch(short=0)
            else:
                self.machine.fetch(short=1)
            machine_ip = raw_input("Input the IP of machine to fire test: ")
            print "Machine Selected ..."
            print "Now showing the testplans availale: "
            self.test.fetch_testplans(0)
            test_plan = raw_input("Enter the test plan number to select to show test cases: ")
            print "Fetching Showing test cases.."
            time.sleep(2)
            print "Test Cases are as follows:"
            self.test.fetch_testcases(test_plan_id=test_plan)
            print "Note: While Entering the multiple template_id, use space in between them"
            a = [int(x) for x in raw_input("Enter the Template ID: ").split()]
            mail = raw_input("Enter the mail ID: ")
            self.execute.collect_ip_and_connect_to_system(machine_ip=machine_ip)
            self.execute.scriptpath_selector(testplan_number=test_plan)
            for list in a:
                self.execute.executor(template_id=list, mail_id=mail)


        else:
            print "Oops Something went wrong ! Try again"
            print ""
            self.main()



print ":::: Welcome to NVTEST ::::"
raw_input("Authorize yourself to system to continue:[Press Enter]")
nv = nvtest()
nv.main()


