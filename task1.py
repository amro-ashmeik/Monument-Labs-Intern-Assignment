import subprocess
import time

#Extends Popen class and adds startTime, endTime, and command fields.
class OProcess(subprocess.Popen):

	def __init__(self, command):
		super().__init__(args=command, stdout=subprocess.PIPE) #PIPE saves output rather than printing it immediately.
		self.startTime = time.time() #Saves creation time of OProcess object.
		self.endTime = None
		self.command = command

#I had to change the 'uptime' command to something else because I'm running Cygwin on Windows and the uptime command would not work.
commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'pwd'
]
processes = []
results = {}

for command in commands:
	proc = OProcess(command)
	processes.append(proc)

#Loops through processes until all are finished.
while processes:
	for proc in processes:
		if proc.poll() is None:
			continue
		else:
			proc.endTime = time.time()
			results[proc.command] = proc.endTime - proc.startTime
			processes.remove(proc)

#maxTime/minTime are the keys to the max/min execution times in results dictionary.
maxTime = max(results, key=results.get)
minTime = min(results, key=results.get)
avgTime = float(sum(results.values())) / len(results)
totalTime = sum(results.values())

print('----REPORT----')
print('Maximum execution time: {}, {}'.format(maxTime, results[maxTime]), 'seconds')
print('Minimum execution time: {}, {}'.format(minTime, results[minTime]), 'seconds')
print('Average execution time: {}'.format(avgTime), 'seconds')
print('Total execution time: {}'.format(totalTime), 'seconds')