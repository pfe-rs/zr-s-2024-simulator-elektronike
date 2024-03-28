import time

class Process:
    def __init__(self, remainingIterations, size, sleepInterval):
        self.remainingIterations = remainingIterations
        self.sleepInterval = sleepInterval
        self.size = size

class CPU:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
            cnt._instance.os = OS()
        return cnt._instance

    def run(self):
        while self.os.hasProcesses():
            proc = self.os.getProcess()
            if not proc:
                time.sleep()
            else:
                while proc.remainingIterations > 0:
                    
                    for i in range(proc.size):
                        continue
                
                    proc.remainingIterations -= 1
                    if proc.sleepInterval > 0: #ako je sleepInterval is 0, no need to sleep
                        self.os.sleep(proc.sleepTime, proc)
                else:
                    self.os.finishProcess(proc)

class CPUScheduler:
    def __init__(self):
        self.processes = []

    def getProcess(self):
        if self.processes:
            return self.processes.pop(0)
        return None

    def putProcess(self, proc):
        self.processes.append(proc)

class OS:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
            cnt._instance.cpu = CPU()
        return cnt._instance

    def __init__(self):
        self.blockedProcesses = []
        self.numberOfProcesses = 0
        _instance.cpuScheduler = CPUScheduler()

    def createProcess(self, proc):
        cpuScheduler.putProcess(proc)

    def hasProcesses(self):
        return self.numberOfProcesses > 0
    
    def getProcess(self):
        return self.cpuScheduler.getProcess()
    
    def sleep(self, proc):
        time.sleep(proc.sleepInterval)
        self.blockedProcesses.append(proc)-
        self.numberOfProcesses += 1

    def finishProcess(self, proc):
        pass
    




os = OS()

process1 = Process(5, 10, 1)
os.createProcess(process1)
process2 = Process(3, 20, 2)
os.createProcess(process2)
process3 = Process(2, 15, 3)
os.createProcess(process3)

cpu = os.cpu
cpu.run()

