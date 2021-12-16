from datetime import datetime
from schedulingJob import *


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
