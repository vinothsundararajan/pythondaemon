import paramiko
import time


startTime = time.time()

open('log.txt', 'w').close()
def file(z):
    f = open("log.txt", "a")
    f.write(z)
    f.write("\n")

start_time="The Start Time is"+" "+time.strftime("%H:%M:%S / %d %b %Y")
file(start_time)

def ssh_comm(ip, usr, passwd, port, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=usr, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for i in stdout:
       li = i.rstrip()
       file(li)
    erro = stderr.readlines()
    print("".join(erro))

ssh_comm('IP', 'root', 'password', 'port', 'cmd')

endTime = time.time()
over_all_time='Took %.2f seconds to complete.' % (endTime - startTime)
file(over_all_time)
