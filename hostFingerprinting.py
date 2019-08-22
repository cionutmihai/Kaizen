import psutil

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)

    return listOfProcObjects

def main():

    print("*** Iterate over all running process and print process ID & Name ***")
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            print(processName , ' ::: ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print('*** Create a list of all running processes ***')

    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
       # Append dict of process detail in list
       listOfProcessNames.append(pInfoDict)

    # Iterate over the list of dictionary and print each elem
    for elem in listOfProcessNames:
        print(elem)

    print('*** Top 5 process with highest memory usage ***')

    listOfRunningProcess = getListOfProcessSortedByMemory()

    for elem in listOfRunningProcess[:5] :
        print(elem)

if __name__ == '__main__':
   main()
