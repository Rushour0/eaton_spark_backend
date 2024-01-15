import os

while (1):
	os.system('ssh -R eaton-spark:80:eaton-flask:5000 serveo.net')
	print('localtunneling is now on')
