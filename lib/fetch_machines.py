import MySQLdb
import os
import sys
from prettytable import PrettyTable
from sql_operations.sql import Sql


class machines:

    def __init__(self):
        self.db = Sql()



    def check_machine_status(self,ip):
        print str(ip)
        response = os.system("ping -c 1 " + str(ip))
        if response == 0:
            return "UP"
        else:
            return "Down"

    def fetch(self,short=0):
        if short == 0:
            machine_query = "select * from machine"
            fields = self.db.query(machine_query)
            table = PrettyTable()
            table.field_names=["Status", "Machine Name", "Owner name", "Machine IP", "Mac Address", "Number of GPUs", "GPUs Connected", "Driver", "Number of Displays", "Displays Connected", "OS Name", "OS Version", "OS Platform", "System Manufacturer", "System Model Name", "Email"]
            for field in fields:
                status = fetch_machine_obj.check_machine_status(field[2])
                table.add_row([status,field[0],field[1],field[2],field[3],field[4],field[5],field[7],field[8],field[9],field[10],field[11],field[12],field[13],field[14],field[15]])
            print table
        elif short == 1:
            machine_query = "select * from machine"
            fields = self.db.query(machine_query)
            table = PrettyTable()
            table.field_names = ["Status", "Machine Name", "Owner name", "Machine IP", "Mac Address"]
            for field in fields:
                status = fetch_machine_obj.check_machine_status(field[2])
                table.add_row([status,field[0],field[1],field[2],field[3]])
            print table



fetch_machine_obj = machines()


fetch_machine_obj.fetch(short=1)

