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
        self.state = 0 #0 = Blocked on I/O, 1 = Running, 2 = Ready
        self.cpuTime = 0
        self.ioTime = 0
        self.processType = processType
        self.burstTime = self.setBurstTime()
        self.remainingBursts = 1
        self.waitTime = 0
        self.pid = pid
        self.justBlocked = 0
        self.waitTill = 0
        self.start_running = 0

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


def FCFS(readyQueue, num_cpu):
    temp = 0
    cpu_num = 0
    cpu = []
    num_process = len(readyQueue)
    cpu = [None for i in range(0,num_cpu)]
    num_finished = 0
    for i in range(0, num_cpu):
        if (len(readyQueue) > 0):
            cpu[i] = readyQueue.pop(0)
    while(len(readyQueue) > 0 and num_finished < num_process):
        #if (temp > 0):
        #    context_switch(temp_process, readyQueue.pop(0))
        #temp= 1
        #cpu_num++;

        for i in range(0, num_cpu):
            if cpu[i]:
                cpu[i].cpuTime+=1
                if cpu[i].burstTime == (time-cpu[i].start_running):
                    cpu[i].justBlocked = 1
                    cpu[i].remainingBursts-=1
                    if remainingBursts == 0:
                        num_finished+=1
                        print "[time " + str(time) + "ms] " + cpu[i].processType + "process ID " + str(cpu[i].pid) + " terminated (turnaround time " + str(time) +  "ms, total wait time " + str(cpu[i].waitTime) + "ms)"
                    else:
                        print "[time " + str(time) + "ms] " + cpu[i].processType + "process ID " + str(cpu[i].pid) + " burst done (turnaround time " + str(time) +  "ms, total wait time " + str(cpu[i].waitTime) + "ms)"


        for i in range(0, num_cpu):
            if cpu[i]:
                if cpu[i].justBlocked == 1:
                    ioTime = random.randint(1000, 4500)
                    cpu[i].ioTime += ioTime
                    cpu[i].wait_til = time + ioTime
                    cpu[i].justBlocked = 0

                if cpu[i].wait_til == time:
                    cpu[i].wait_til = 0
                    if cpu[i].remainingBursts > 0 :
                        readyQueue.append(cpu[i])
                    if len(readyQueue) > 0:
                        temp_p = readyQue.pop(0)
                        context_switch(cpu[i], temp_p) #implment context switch
                        cpu[i] = temp_p
                        cpu[i].start_running = time
                    else:
                        cpu[i] = None


        for p in readyQueue:
            p.waitTime+=1

        time+= 1

    return 0

def SJF(readyQueue, num_cpu):
    return 0

def SJF_preemption(readyQueue, num_cpu):
    return 0

def Round_Robin(readyQueue, tslice, num_cpu):
    return 0


if __name__ == '__main__':
    num_proc = 12
    num_cpu = 4
    tSlice = 80
    processes = []
    readyQueue = []
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



    for i in range(1,num_proc+1):
        if i <= (num_proc * 4/5):
            processes.append(Process("interactive",i))
        else:
            processes.append(Process("cpuBound",i))

    for p in processes:
        readyQueue.append(p)
        if(p.processType == "interactive"):
            print "[time " + str(time) + "ms] Interactive process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) +  "ms CPU time)"
        else:
            print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) + "ms CPU time)"


    #time = context_switch(readyQueue[0], readyQueue[1], time)


    print "Yay "
