from userInput import *
from schedulingJob import *

jobs = []
executionWindow = None

while True:
    if jobs:
        print(jobs)
    if executionWindow is not None:
        print(f"{str(executionWindow[0])}, {str(executionWindow[1])}")
    value = userMainInput()
    if value == 1:
        job = userJobInput()
        for j in jobs:
            if j.id == job.id:
                print("Id informado já existe.")
                break
            else:
                jobs.append(userJobInput())
                break
    elif value == 2:
        idToRemove = userRemoveInput()
        for j in jobs:
            if j.id == idToRemove:
                jobs.remove(j)
                print("Job removido com sucesso!.")
                break
    elif value == 3:
        executionWindow = userExecutionWindowInput()
    elif value == 4:
        print(*getJobExecutionSet(jobs, executionWindow), sep='\n')
        print('\n')
    elif value == 5:
        exit(0)
    else:
        print("Entre com um valor válido.")
