import sys
import os
import subprocess
import MySQLdb
from sql_operations.sql import Sql
import paramiko
import spur

class Execute:

    _pypath = ""
    _scpath = ""

    def __init__(self):
        mkdir = "mkdir /mnt/atp"
        mount = "mount netapp-pu02:/vol/projects8/linuxqa-pune /mnt/atp/"
        subprocess.call([mkdir], shell=True)
        subprocess.call([mount], shell=True)
        print ":: ATP Mounted ::"
        self._pypath = "/mnt/atp/people-local/atifs/ActivePython-2.7.2.5-linux-x86_64/INSTALLDIR/bin"
        self.db = Sql()



    def scriptpath_selector(self, testplan_number):
        path_query = "select path from testplans where testplans.index={0}".format(testplan_number)
        result = self.db.query(path_query)
        for field in result:
            self._scpath = field[0]

    def collect_ip_and_connect_to_system(self,machine_ip):
        try:
            self.client = paramiko.Transport(machine_ip,22)
            # self.client.load_system_host_keys()
            # self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(username="root",password="nvidia123")
            print "Connected"
        except:
            print "Unable to connect"

    def executor(self,template_id, mail_id):
        try:
            # cd_command = "cd {0}".format(self._pypath)
            # self.client.exec_command(cd_command)
            temp = ""
            self._scpath = "/mnt/atp/people-local/atifs/project/"
            command_exec = "sh {0}graphics.sh {1} {2}".format(self._scpath,mail_id,template_id)
            print command_exec
            session = self.client.open_channel("session")
            session.exec_command(command_exec)
            session.recv_exit_status()
            while session.recv_ready():
                temp += session.recv(1024)
                print temp

        except Exception,e:
            print "Error: "+str(e)
        # os.chdir(self._pypath)
        # execute_command = "./python {0} -m {1} -t {2}".format(self._scpath,mail_id,template_id)
        # print "Executing...."
        # subprocess.call([execute_command],shell=True)


execute_obj = Execute()
execute_obj.collect_ip_and_connect_to_system("10.24.141.133")
execute_obj.scriptpath_selector(1)
execute_obj.executor("1120263", "afaraz@nvidia.com")





