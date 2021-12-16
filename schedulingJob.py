from datetime import datetime, timedelta
from operator import methodcaller
DAILY_EXECUTION_LENGTH = 8


class Job:
    def __init__(self):
        self.id = 0
        self.description = ""
        self.maxCompletionDate = datetime.now()
        self.estimatedExecutionDuration = 0

    def maxStartDate(self):
        return self.maxCompletionDate - timedelta(hours=self.estimatedExecutionDuration)


def sortJobsByCompletionDateTime(jobs):
    jobs.sort(key=methodcaller('maxStartDate'))


def checkIfValidJobForExecution(job, execution_window, available_execution_length):
    return job.estimatedExecutionDuration < available_execution_length \
           and job.maxStartDate() > execution_window[0] \
           and job.maxCompletionDate < execution_window[1]


def getJobExecutionSet(sorted_jobs, execution_window):
    jobExecutionSet = []
    array = []
    availableExecutionTime = DAILY_EXECUTION_LENGTH
    for job in sorted_jobs:
        if checkIfValidJobForExecution(job, execution_window, availableExecutionTime):
            availableExecutionTime -= job.estimatedExecutionDuration
            array.append(job)
        else:
            jobExecutionSet.append(array.copy())
            array = []
            availableExecutionTime = DAILY_EXECUTION_LENGTH
    return jobExecutionSet


