from datetime import timedelta
from operator import methodcaller

DAILY_EXECUTION_LENGTH = 8


class Job:
    def __init__(self, new_id, description, max_completion_date, estimated_execution_duration):
        self.id = new_id
        self.description = description
        self.maxCompletionDate = max_completion_date
        self.estimatedExecutionDuration = estimated_execution_duration

    def __repr__(self):
        return f"{self.id}|{self.description}|{self.maxCompletionDate}|{self.estimatedExecutionDuration}"

    def maxStartDate(self):
        return self.maxCompletionDate - timedelta(hours=self.estimatedExecutionDuration)


def sortJobsByStartDateTime(jobs_to_sort):
    jobs_to_sort.sort(key=methodcaller('maxStartDate'))


def checkIfValidJobForExecution(job_to_check, execution_window, available_execution_length):
    return job_to_check.estimatedExecutionDuration <= available_execution_length \
           and job_to_check.maxStartDate() >= execution_window[0] \
           and job_to_check.maxCompletionDate <= execution_window[1]


def getJobExecutionSet(jobs_to_organize, execution_window):
    if not jobs_to_organize:
        return "Não há jobs para agendar.\n"
    if execution_window is None:
        return "Não há janela de execução.\n"
    jobExecutionSet = []
    array = []
    availableExecutionTime = DAILY_EXECUTION_LENGTH
    sortJobsByStartDateTime(jobs_to_organize)
    for job_to_organize in jobs_to_organize:
        if checkIfValidJobForExecution(job_to_organize, execution_window, availableExecutionTime):
            availableExecutionTime -= job_to_organize.estimatedExecutionDuration
            array.append(job_to_organize)
        else:
            jobExecutionSet.append(array.copy())
            array = [job_to_organize]
            availableExecutionTime = DAILY_EXECUTION_LENGTH - job_to_organize.estimatedExecutionDuration
    jobExecutionSet.append(array.copy())
    return jobExecutionSet

