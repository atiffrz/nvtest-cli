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
        self.client = paramiko.SSHClient()


    def scriptpath_selector(self, testplan_number):
        path_query = "select path from testplans where index={0}".format(testplan_number)
        result = self.db.query(path_query)
        for field in result:
            self._scpath = field[0]

    def collect_ip_and_connect_to_system(self,machine_ip):
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(machine_ip,username="root",password="nvidia123")
        print "connected"


    def executor(self,template_id, mail_id):
        os.chdir(self._pypath)
        execute_command = "./python {0} -m {1} -t {2}".format(self._scpath,mail_id,template_id)
        print "Executing...."
        subprocess.call([execute_command],shell=True)


execute_obj = Execute()
execute_obj.collect_ip_and_connect_to_system("10.24.142.132")
# execute_obj.scriptpath_selector(1)
# execute_obj.executor("1120263", "afaraz@nvidia.com")





