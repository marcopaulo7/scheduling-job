import unittest
from schedulingJob import *
from datetime import datetime

testArray = [Job(1, 'Importação de arquivos de fundos', datetime.fromisoformat('2019-11-10 12:00:00'), 2),
             Job(2, 'Importação de dados da Base Legada', datetime.fromisoformat('2019-11-11 12:00:00'), 4),
             Job(3, 'Importação de dados de integração', datetime.fromisoformat('2019-11-11 08:00:00'), 6)]

testExecutionWindow = (datetime.fromisoformat("2019-11-10 09:00:00"), datetime.fromisoformat("2019-11-11 12:00:00"))


class TestJobScheduler(unittest.TestCase):
    def testSortByCompletionDate(self):
        sortedArray = [Job(1, 'Importação de arquivos de fundos', datetime.fromisoformat('2019-11-10 12:00:00'), 2),
                       Job(3, 'Importação de dados de integração', datetime.fromisoformat('2019-11-11 08:00:00'),
                           6),
                       Job(2, 'Importação de dados da Base Legada', datetime.fromisoformat('2019-11-11 12:00:00'),
                           4)]
        sortJobsByStartDateTime(testArray)
        self.assertEqual(str(testArray), str(sortedArray))

    def test_job_validation_check(self):
        firstInvalidJob = Job(5, 'Job invalido 1', datetime.fromisoformat('2012-11-10 12:00:00'), 2)
        secondInvalidJob = Job(6, 'Job invalido 2', datetime.fromisoformat('2020-11-10 12:00:00'), 2)
        thirdInvalidJob = Job(7, 'Job invalido 3', datetime.fromisoformat('2019-11-10 12:00:00'), 10)
        self.assertTrue(checkIfValidJobForExecution(testArray[0], testExecutionWindow, DAILY_EXECUTION_LENGTH))
        self.assertFalse(checkIfValidJobForExecution(firstInvalidJob, testExecutionWindow, DAILY_EXECUTION_LENGTH))
        self.assertFalse(checkIfValidJobForExecution(secondInvalidJob, testExecutionWindow, DAILY_EXECUTION_LENGTH))
        self.assertFalse(checkIfValidJobForExecution(thirdInvalidJob, testExecutionWindow, DAILY_EXECUTION_LENGTH))

    def test_execution_set_getter(self):
        secondTestArray = [Job(8, 'Job teste 8', datetime.fromisoformat('2019-11-10 17:00:00'), 8),
                           Job(9, 'Job teste 9', datetime.fromisoformat('2019-11-10 20:00:00'), 5),
                           Job(10, 'Job teste 10', datetime.fromisoformat('2019-11-11 04:00:00'), 3),
                           Job(11, 'Job teste 11', datetime.fromisoformat('2019-11-11 07:00:00'), 2)]

        resultTestArray = [
            [Job(1, 'Importação de arquivos de fundos', datetime.fromisoformat('2019-11-10 12:00:00'), 2),
             Job(3, 'Importação de dados de integração', datetime.fromisoformat('2019-11-11 08:00:00'), 6)],
            [Job(2, 'Importação de dados da Base Legada', datetime.fromisoformat('2019-11-11 12:00:00'), 4)]]

        secondResultTestArray = [[Job(8, 'Job teste 8', datetime.fromisoformat('2019-11-10 17:00:00'), 8)],
                                 [Job(9, 'Job teste 9', datetime.fromisoformat('2019-11-10 20:00:00'), 5),
                                  Job(10, 'Job teste 10', datetime.fromisoformat('2019-11-11 04:00:00'), 3)],
                                 [Job(11, 'Job teste 11', datetime.fromisoformat('2019-11-11 07:00:00'), 2)]]
        sortJobsByStartDateTime(testArray)
        sortJobsByStartDateTime(secondTestArray)
        self.assertEqual(str(getJobExecutionSet(testArray, testExecutionWindow)), str(resultTestArray))
        self.assertEqual(str(getJobExecutionSet(secondTestArray, testExecutionWindow)), str(secondResultTestArray))