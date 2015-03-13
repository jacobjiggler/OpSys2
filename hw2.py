#Jacob Martin
#Satoshi Matsuura

import random, sys, copy
# Time for context switching
tcs = 4
#global time
time = 0

# Interactive, cpu bound
class Process:
    def __init__ (self, processType, pid):
        self.processType = processType
        self.burstTime = self.setBurstTime()
        self.remainingBursts = 1
        self.waitTime = 0
        self.pid = pid
        
        if self.processType == "cpuBound":
            self.remainingBursts = 6
        

    def setBurstTime(self):
        # Sets random burst time for cpu bound or interactive
        if (self.processType == "interactive"):
            return random.randint(20, 200)
        elif(self.processType == "cpuBound"):
            return random.randint(1000, 4500)
        else:
            raise Exception("Invalid Process Type")

def context_switch(processA, processB, time):
    print "[time " + str(time) + "ms] Context switch (swapping out Process ID " + str(processA.pid) + " for Process ID " + str(processB.pid) +")"
    time+=tcs
    return time
    
def FCFS(readyQueue):
    
    return 0

def SJF(readyQueue):
    return 0

def SJF_preemption(readyQueue):
    return 0

def Round_Robin(readyQueue, tcs):
    return 0


if __name__ == '__main__':
    num_proc = 12
    num_cpu = 4
    tSlice = 80
    processes = []
    readyQueue = []
    cpu = []
    turnaround = []
    total_wait_time = []
    

    #arg[0] is the file, 
    #arg[1] is optional num_proc, 
    #arg[2] is optional numuber of cpu
    #arg[3] is optional time slice for RR
    if len(sys.argv) != 1:
        if len(sys.argv) > 1 and len(sys.argv) >= 2:
            if sys.argv[1]:
                num_proc = int(sys.argv[1])
        if len(sys.argv) > 1 and len(sys.argv) >= 3:
            if sys.argv[2]:
                num_cpu = int(sys.argv[2])
        if len(sys.argv) > 1 and len(sys.argv) >= 4:
            if sys.argv[3]:
                tSlice = int(sys.argv[3])
                
    
    cpu = [None for i in range(0,num_cpu)]
    for i in range(1,num_proc+1):
        if i <= (num_proc * 4/5):
            processes.append(Process("interactive",i))
        else:
            processes.append(Process("cpuBound",i))
    
    random.shuffle(processes)
    for p in processes:
        readyQueue.append(p)
        if(p.processType == "interactive"):
            print "[time " + str(time) + "ms] Interactive process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) +  "ms CPU time)"
        else:
            print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) + "ms CPU time)"
    
    
    #time = context_switch(readyQueue[0], readyQueue[1], time)
    
    
    print "Yay "
    

