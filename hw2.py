#Jacob Martin
#Satoshi Matsuura

import random, sys, copy

# Interactive, cpu bound
class Process:
    def __init__ (self, processType, pid):
        self.cpuTime = 0
        self.ioTime = 0
        self.processType = processType
        self.burstTime = self.setBurstTime()
        self.burstTimeLeft = self.burstTime
        self.totalBurstTime = 0
        self.totalWaitTime = 0
        self.remainingBursts = 1
        self.waitTime = 0
        self.pid = pid
        self.justBlocked = 0
        self.waitTill = 0


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

def find_longest(cpu):
    index = 0;
    longest_burst = cpu[0].burstTimeLeft
    for i in range(0, len(cpu)):
        if longest_burst < cpu[i].burstTimeLeft: 
            longest_burst = cpu[i].burstTimeLeft
            index = i
    
    return index
        


def FCFS(readyQueue, num_cpu):
    output = list(readyQueue)
    time = 0
    tcs = 4
    cpu = []
    waitQueue = []
    num_process = len(readyQueue)
    cpu = [None for i in range(0,num_cpu)]
    num_finished = 0
    for i in range(0, num_cpu):
        if (len(readyQueue) > 0):
            cpu[i] = readyQueue.pop(0)

    while(len(readyQueue) > 0 or num_finished < num_process):
        time+=1
        for i in range(0, num_cpu):
            if cpu[i]:
                cpu[i].cpuTime+=1
                cpu[i].burstTimeLeft-=1
                if cpu[i].burstTimeLeft == 0:
                    cpu[i].justBlocked = 1
                    cpu[i].remainingBursts-=1
                    if cpu[i].remainingBursts == 0:
                        num_finished+=1
                        if (cpu[i].processType == "interactive"):
                            print "[time " + str(time) + "ms] " + cpu[i].processType + "process ID " + str(cpu[i].pid) + " burst done (turnaround time " + str(cpu[i].burstTime + cpu[i].waitTime) +  "ms, total wait time " + str(cpu[i].waitTime) + "ms)"
                        else:
                            print "[time " + str(time) + "ms] " + cpu[i].processType + "process ID " + str(cpu[i].pid) + " terminated (avg turnaround time " + "%.3f" % (float(cpu[i].totalBurstTime) / 6) +  "ms, avg total wait time " + "%.3f" % (float(cpu[i].totalWaitTime) / 6) + "ms)"
                    else:
                        #add burst and wait times to totals
                        cpu[i].totalBurstTime+= cpu[i].burstTime
                        cpu[i].totalWaitTime+= cpu[i].waitTime
                        print "[time " + str(time) + "ms] " + cpu[i].processType + "process ID " + str(cpu[i].pid) + " burst done (turnaround time " + str(cpu[i].burstTime + cpu[i].waitTime) +  "ms, total wait time " + str(cpu[i].waitTime) + "ms)"


        for i in range(0, num_cpu):
            if cpu[i]:
                if cpu[i].justBlocked == 1:
                    ioTime = random.randint(1000, 4500)
                    cpu[i].ioTime += ioTime
                    cpu[i].waitTill = time + ioTime
                    #print "I/O time is " + str(ioTime)
                    cpu[i].justBlocked = 0
                    if cpu[i].remainingBursts > 0 :
                        waitQueue.append(cpu[i])

                    if len(readyQueue) > 0:
                        temp_p = readyQueue.pop(0)
                        context_switch(cpu[i], temp_p, time) #implment context switch
                        temp_p.cpuTime -= 4
                        temp_p.burstTimeLeft += 4
                        cpu[i] = temp_p
                    elif(len(readyQueue)==0 and len(waitQueue)==0):
                        cpu[i] = None
        
        temp = 0
        for i in range(0, len(waitQueue)):
            if waitQueue[i].waitTill == time:
                waitQueue[i].waitTime = 0
                waitQueue[i].setBurstTime()
                waitQueue[i].burstTimeLeft = p.burstTime
                print "[time " + str(time) + "ms] CPU-bound process ID " + str(waitQueue[i].pid) + " entered ready queue (requires " + str(waitQueue[i].burstTime) + "ms CPU time)"
                readyQueue.append(waitQueue[i])
                temp = i
        
        if temp!= 0:
            waitQueue.pop(temp)

        for p in readyQueue:
            p.waitTime+=1



    total_turnaround = 0
    total_wait = 0
    min_turnaround = output[0].waitTime + output[0].burstTime
    max_turnaround = output[0].waitTime + output[0].burstTime
    min_wait = output[0].waitTime
    max_wait = output[0].waitTime

    for p in output:
        temp_wait = p.waitTime
        temp_turnaround = (p.waitTime+p.burstTime)
        total_wait += temp_wait
        total_turnaround+= temp_turnaround
        if temp_turnaround < min_turnaround:
            min_turnaround = temp_turnaround
        if temp_turnaround > max_turnaround:
            max_turnaround = temp_turnaround
        if temp_wait < min_wait:
            min_wait = temp_wait
        if temp_wait > max_wait:
            max_wait = temp_wait

    avg_turnaround = float(total_turnaround)/len(output)
    avg_wait = float(total_wait)/len(output)
    print "Turnaround time: min " + str(min_turnaround) + "ms; avg " + "%.3f" % (avg_turnaround) + "ms; max " + str(max_turnaround) + "ms"
    print "Total wait time: min " + str(min_wait) + "ms; avg " + "%.3f" % (avg_wait) + "ms; max " + str(max_wait) + "ms"

    total_cpu_time = 0
    total_IO_time = 0
    for p in output:
        total_cpu_time+=p.cpuTime

    print "Average CPU utilization: %.3f%%" % (total_cpu_time/float(time*num_cpu)*100)
    print ""
    print "Average CPU utilization per process"
    for p in output:
        print "process ID %d: %.3f%%" %(p.pid , p.cpuTime/float(time * num_cpu) * 100)


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
    time = 0


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
    random.shuffle(processes)

    pid_id = 1
    for p in processes:
        p.pid = pid_id
        readyQueue.append(p)
        pid_id+=1
        if(p.processType == "interactive"):
            print "[time " + str(time) + "ms] Interactive process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) +  "ms CPU time)"
        else:
            print "[time " + str(time) + "ms] CPU-bound process ID " + str(p.pid) + " entered ready queue (requires " + str(p.burstTime) + "ms CPU time)"

    print "-------------------First Come First Served-------------------"
    FCFS(readyQueue, num_cpu)




    print "Yay "
