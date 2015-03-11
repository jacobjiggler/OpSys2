import rand, Queue

# Time for context switching
tcs = 4


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
