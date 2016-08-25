
import MySQLdb
import csv
from itertools import islice
import os



class Database:

    host = 'localhost'
    user = 'root'
    password = 'nvidia123'
    db = 'nvidia'
    insert_state = ''
    update_sql = ""


    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query,mac,system_ip):
        print query
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            insert_state =  'Conflict'
            status = db.check_machine_status(system_ip)
            update_sql = 'update machine set machine_ip ="{0}", status="{1}"  where mac_address="{2}"'.format(system_ip,status,mac)
            db.update(insert_state,update_sql)
            print "-----------------Inserted Successfully--------------------"
            # print update
            self.connection.rollback()

    def update(self,insert_state,statement):
        if insert_state == 'Conflict':
            print insert_state,statement
            try:
                self.cursor.execute(statement)
                self.connection.commit()
            except:
                self.connection.rollback()


    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        print "Conflict Mac IP Updated"
        # return cursor.fetchall()

    def __del__(self):
        self.connection.close()

    def check_machine_status(self,ip):
        print str(ip)
        response = os.system("ping -c 1 " + str(ip))
        if response == 0:
            return "UP"
        else:
            return "Down"

    def retrieving_and_entering_data(self):
        path = "/mnt/atp/people-local/pratiks/softwares/NVTEST/"

        with open(path + "database.csv", "rb") as fp:
            reader = csv.DictReader(fp)
            l = list(reader)
            length =  len(l)
            for i in range(0,length):
                data = l[i]
                machine_name = data.get("Machine_Name")
                owner_name = data.get("Owner_Name")
                machine_ip = data.get("Machine_IP")
                mac = data.get("Mac_Address")
                number_of_gpus = data.get("Number_of_GPU")
                gpus_connected = data.get("GPU_connected")
                status = db.check_machine_status(machine_ip)
                driver = data.get("Driver")
                no_of_displays = data.get("Number_of_displays")
                displays_connected = data.get("Display_Connected")
                os_name = data.get("OS_Name")
                os_version = data.get("OS_Version")
                os_platform = data.get("OS_Platform")
                system_manufacturer = data.get("System_Manufacturer")
                system_model_name = data.get("System_Model_Name")
                email = data.get("Email_address")
                msg = '"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}","{14}","{15}"'.format(machine_name,owner_name,machine_ip,mac,number_of_gpus,gpus_connected,status,driver,no_of_displays,displays_connected,os_name,os_version,os_platform,system_manufacturer,system_model_name,email)
                sql = 'insert into machine values('+msg+')'
                db.insert(sql,mac,machine_ip)







if __name__ == "__main__":

    db = Database()
    mac = ''
    ip = ''
    #CleanUp Operation
    # del_query = "DELETE FROM basic_python_database"
    # db.insert(del_query)

    # Data Insert into the table
    # query = "insert into machines values('10.24.142.7','root','nvidia123')"
    #
    #
    # # db.query(query)
    # db.insert(query)

   # Data retrieved from the table
   #  select_query = "select * from machines"
   # #
   #  people = db.query(select_query)
   # #
   #  for person in people:
   #     print person['machine_ip']+"  "+person['machine_uname']+"  "+person['machine_passwd']
   # #
    db.retrieving_and_entering_data()
