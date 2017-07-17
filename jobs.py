
from optparse import OptionParser
import time,sys,threading,logging,random,os

def usage():
	print(''' \033[0m	\033[97m''')
	print(''' \033[01m	    ..__Xjobs __..\033[0m''')

	print(''' \033[0m	\033[91m''')
	print(''' \033[01m	USAGE\033[0m''')


	print ('''
	$ \033[33mXjobs
	  ps aux | grep firefox
	  python kelly.py
	  g++ main.cpp
	  g++ sqaresum.cpp
	  clear \033[0m''')

	print(''' \033[0m	\033[91m''')
	print(''' \033[92m	Press Enter twice when after inputs\033[0m''')
	print(''' \033[92m	type exit() to exit the code \033[0m''')





def execute(job):
	try:
		o = os.system(job)
		if o:
			o = o/0
		print(''' \033[32m Running '''+job+''' ...... \033[0m''')
	except:
		print(''' \033[31m'''+job+''' is not valid job\033[0m''')

def main(n, jobs):
	print(''' \033[0m	\033[91m''')
	print(''' \033[92m	Running in '''+str(len(jobs))+''' threads\033[0m''')
	for job in jobs:
		t = threading.Thread(target = execute, args=(job,))
		t.start()

def get_parameters():
	usage()
	jobs = []
	try:
		j = input()
	except Exception as e :
		print(e)

	if 'exit' in j or 'quit' in j:
		sys.exit()
	while j:
		jobs.append(j)
		j = input()
		if 'exit' in j or 'quit' in j:
			sys.exit()
	JOBS = []
	JOBS.append(jobs[:100])

	for i in range(int(len(jobs)/ 100) - 1):
		JOBS.append(jobs[(i+1)*100:(i+2)*100])

	for jobs in JOBS:
		main(len(jobs), jobs)


os.system("clear")
get_parameters()

