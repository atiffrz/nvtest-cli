import paramiko
import os
import sys

temp = ""

trans = paramiko.Transport(("10.24.141.133", 22))
trans.connect(username="root", password="nvidia123")
session = trans.open_channel("session")
command = "sh /mnt/atp/people-local/atifs/project/graphics.sh afaraz@nvidia.com 1120263"
print session.exec_command(command)
session.recv_exit_status()
while session.recv_ready():
    temp += session.recv(1024)
    print temp