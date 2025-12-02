from collections import deque
from unittest import TestCase,main

from project.railway_station import RailwayStation

class RailwayStatioTest(TestCase):
    name = 'Test'

    def setUp(self):
        self.test_train = RailwayStation('Test')

    def test_init(self):
        self.assertEqual('Test',self.test_train.name)
        self.assertEqual(deque(),self.test_train.arrival_trains)
        self.assertEqual(deque(),self.test_train.departure_trains)

    def test_name_init_name_too_short(self):
        with self.assertRaises(ValueError) as ve:
            self.test_train.name = 'ABC'
        self.assertEqual("Name should be more than 3 symbols!",str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_train.name = 'AB'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_train.name = ''
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))


    def test_new_arrival_on_board(self):
        self.test_train.new_arrival_on_board('BANANA')
        self.assertEqual(deque(['BANANA']),self.test_train.arrival_trains)
        self.assertEqual(1,len(self.test_train.arrival_trains))

        self.test_train.arrival_trains = deque(['Test1','Test2'])
        self.test_train.new_arrival_on_board('Test3')
        self.assertEqual(deque(['Test1','Test2','Test3']),self.test_train.arrival_trains)
        self.assertEqual(3,len(self.test_train.arrival_trains))

    def test_train_has_arrived_train_in_arrivals(self):
        self.test_train.arrival_trains = deque(['Test1','Test2','Test3'])

        result = self.test_train.train_has_arrived('Test1')
        self.assertEqual(f"Test1 is on the platform and will leave in 5 minutes.",result)
        self.assertEqual(deque(['Test2','Test3']),self.test_train.arrival_trains)
        self.assertEqual(deque(['Test1']),self.test_train.departure_trains)

        result = self.test_train.train_has_arrived('Test2')
        self.assertEqual(f"Test2 is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['Test3']), self.test_train.arrival_trains)
        self.assertEqual(deque(['Test1','Test2',]), self.test_train.departure_trains)

    def test_train_has_arrived_train_not_in_arrivals_not_in_deque(self):
        self.test_train.arrival_trains = deque(['Test1', 'Test2', 'Test3'])

        result = self.test_train.train_has_arrived('Test4')
        self.assertEqual(f"There are other trains to arrive before Test4.",result)
        self.assertEqual(deque(['Test1', 'Test2', 'Test3']), self.test_train.arrival_trains)

    def test_train_has_arrived_train_not_in_arrivals_in_deque(self):
        self.test_train.arrival_trains = deque(['Test1', 'Test2', 'Test3'])

        result = self.test_train.train_has_arrived('Test2')
        self.assertEqual(f"There are other trains to arrive before Test2.", result)
        self.assertEqual(deque(['Test1', 'Test2', 'Test3']), self.test_train.arrival_trains)


    def test_train_has_left_returns_true(self):
        self.test_train.departure_trains = deque(['Test1', 'Test2'])
        result = self.test_train.train_has_left('Test1')
        self.assertTrue(result)
        self.assertEqual(deque(['Test2']),self.test_train.departure_trains)

    def test_train_has_left_returns_false(self):
        self.test_train.departure_trains = deque(['Test1', 'Test2'])

        result = self.test_train.train_has_left('Test3')

        self.assertFalse(result)
        self.assertEqual(deque(['Test1', 'Test2']),self.test_train.departure_trains)
