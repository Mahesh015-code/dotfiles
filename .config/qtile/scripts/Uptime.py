from cgitb import text
from distutils import text_file
import time, os
import datetime
""" print(time.time())
system_time= time.localtime(time.time())
print(system_time) """ # This for find the local time defined by the system
# m = os.system(cmd) # It can not store the output of the file

cmd = 'uptime -p'
m = os.popen(cmd)

# system_time= time.localtime(time.time()) this is a python code to get the corrent uptime
system_time = os.popen("date")
# print("The system shutdowned at ", system_time.read())
# print(m.read())
now = datetime.datetime.now()
text_file = open(r"/home/mahesh/Documents/Second brain/3.Resources/Journals/Daily Jorunal/"+"%s-%s-%s.md"%(now.year,now.month,now.day),"+a")
text_file.write(m.read())
text_file.close()
# print("the date is"+"xyz %s-%s-%s"%(now.year,now.month,now.day))
os.system("sleep 1.5")
os.system("shutdown now")
