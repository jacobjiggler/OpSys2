#Jacob Martin
#Satoshi Matsuura


import rand, Queue, sys, copy

# Time for context switching
tcs = 4
#global time
time = 0


readyQueue = Queue.Queue()


# Interactive, cpu bound
class Process:

    def __init__(self, processType = "interactive"):
        self.processType = processType
        self.burstTime = self.setBurstTime()
        self.remainingBursts = 1

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
	processes = []

	#arg[0] is the file, arg[1] is optional num_proc, arg[2] is optional numuber of cpu
	if len(sys.argv) != 1:
		if len(sys.argv) > 1 and len(sys.argv) <= 3:
			if sys.argv[1]:
				num_proc = int(sys.argv[1])
			if sys.argv[2]:
				num_cpu = int(sys.argv[2])
