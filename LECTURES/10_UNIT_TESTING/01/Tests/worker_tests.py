from Tests.worker import Worker
from unittest import TestCase
from unittest import main

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Patar',1000,10)

    def test_worker_credentials(self):
       result = (self.worker.name,self.worker.salary,self.worker.energy)
       expected = ('Patar',1000,10)
       self.assertEqual(expected,result)

    def test_worker_rest(self):
        self.worker.rest()
        result = self.worker.energy

        expected = 11
        self.assertEqual(expected,result)

    def test_negative_energy(self):
        result = self.worker.work()
        expected = 'Not enough energy.'

        self.assertEqual(expected,result)

        self.assertEqual(expected,result)
        self.worker.energy = 10

    def test_work_money_raise(self):
        expected = self.worker.money + self.worker.salary

        self.worker.work()
        result = self.worker.money

        self.assertEqual(expected,result)

    def test_worker_emergy(self):
        expected = 9

        self.worker.work()
        result = self.worker.energy

        self.assertEqual(expected,result)

    def test_get_info(self):
        expected = f'Patar has saved 1000 money.'
        result = self.worker.get_info()

        self.assertEqual(expected,result)
