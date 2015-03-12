#Jacob Martin
#Satoshi Matsuura

import random, Queue, sys, copy


# Time for context switching
tcs = 4
#global time
time = 0

readyQueue = Queue.Queue()


# Interactive, cpu bound
class Process:

    def __init__(self, processType = "interactive", pid):
        self.processType = processType
        self.burstTime = self.setBurstTime()
        self.remainingBursts = 1
		self.waitTime = 0
		self.pid = pid
		
        if self.processType == "cpuBound":
            self.remainingBursts = 6
		

    def setBurstTime(self):
        # Sets random burst time for cpu bound or interactive
        if (self.processType != "interactive" or self.processType != "cpuBound"):
            raise Exception("Invalid Process Type")
        if (self.processType == "interactive"):
            return rand.randint(20, 200)
        elif(self.processType == "cpuBound"):
            return rand.randint(1000, 4500)

if __name__ == '__main__':
	num_proc = 12
	num_cpu = 4
	tSlice = 80
	processes = []
	cpu = []
	turnaround = []
	total_wait_time = []
	

	#arg[0] is the file, 
	#arg[1] is optional num_proc, 
	#arg[2] is optional numuber of cpu
	#arg[3] is optional time slice for RR
	if len(sys.argv) != 1:
		if len(sys.argv) > 1 and len(sys.argv) <= 4:
			if sys.argv[1]:
				num_proc = int(sys.argv[1])
			if sys.argv[2]:
				num_cpu = int(sys.argv[2])
			if sys.argv[3]:
				tSlice = int(sys.argv[3])
	
	
	

