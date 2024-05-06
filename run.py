import os

while (1):
	os.system('ssh -R eaton-spark:80:localhost:6000 serveo.net')
	print('localtunneling is now on')
