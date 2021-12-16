from datetime import datetime, timedelta
from operator import methodcaller
DAILY_EXECUTION_LENGTH = 8


class Job:
    def __init__(self, id, description, max_completion_date, estimated_execution_duration):
        self.id = id
        self.description = description
        self.maxCompletionDate = max_completion_date
        self.estimatedExecutionDuration = estimated_execution_duration

    def __repr__(self):
        return f"{self.id}|{self.description}|{self.maxCompletionDate}|{self.estimatedExecutionDuration}"

    def maxStartDate(self):
        return self.maxCompletionDate - timedelta(hours=self.estimatedExecutionDuration)


def sortJobsByCompletionDateTime(jobs_to_sort):
    jobs_to_sort.sort(key=methodcaller('maxStartDate'))


def checkIfValidJobForExecution(job, execution_window, available_execution_length):
    return job.estimatedExecutionDuration <= available_execution_length \
           and job.maxStartDate() >= execution_window[0] \
           and job.maxCompletionDate <= execution_window[1]


def getJobExecutionSet(jobs_to_organize, execution_window):
    if not jobs_to_organize:
        return "Não há jobs para agendar.\n"
    if execution_window is None:
        return "Não há janela de execução.\n"
    jobExecutionSet = []
    array = []
    availableExecutionTime = DAILY_EXECUTION_LENGTH
    sortJobsByCompletionDateTime(jobs_to_organize)
    for job in jobs_to_organize:
        if checkIfValidJobForExecution(job, execution_window, availableExecutionTime):
            availableExecutionTime -= job.estimatedExecutionDuration
            array.append(job)
        else:
            jobExecutionSet.append(array.copy())
            array = [job]
            availableExecutionTime = DAILY_EXECUTION_LENGTH - job.estimatedExecutionDuration
    jobExecutionSet.append(array.copy())
    return jobExecutionSet


def userMainInput():
    print("Tecle 1 para entrar com um novo job")
    print("Tecle 2 para remover um job")
    print("Tecle 3 para informar a janela de execução")
    print("Tecle 4 para organizar a execução dos jobs")
    print("Tecle 5 para sair")
    return validateInput("Entre com um valor: ", "Valor inválido!", int)


def userJobInput():
    jobId = validateInput("\nEntre com o id do job: ", "Erro! Entre com um número válido para o id", int)
    description = validateInput("Entre com a descrição do job: ", "Erro! Entre com uma descrição válida", str)
    maxCompletionDate = validateInput("Entre com a data/hora (yyyy-MM-dd hh:mm:ss) limite para conclusão do job: ",
                                   "Erro! Entre com um valor válido para a data", datetime.fromisoformat)
    estimatedExecutionDuration = validateInput("Entre com a duração do job em horas: ",
                                            "Erro! Entre com um número válido para a quantidade de horas", int)
    print("\n")
    return Job(jobId, description, maxCompletionDate, estimatedExecutionDuration)


def userExecutionWindowInput():
    startDate = validateInput("Entre com a data/hora (yyyy-MM-dd hh:mm:ss) de inicio da execução dos jobs: ",
                              "Erro! Entre com uma data/hora válida", datetime.fromisoformat)
    endDate = validateInput("Entre com a data/hora (yyyy-MM-dd hh:mm:ss) de fim da execução dos jobs: ",
                            "Erro! Entre com uma data/hora válida", datetime.fromisoformat)
    return startDate, endDate


def userRemoveInput():
    return validateInput("\nEntre com o id do job a ser removido: ", "Erro! Entre com um número válido para o id", int)


def validateInput(inputMessage, errorMessage, value_type):
    while True:
        try:
            inputted = value_type(input(inputMessage))
        except ValueError:
            print(errorMessage)
            continue
        else:
            return inputted


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


