from unittest import TestCase,main

from project.trip import Trip

class TripTest(TestCase):
    budget = 20000
    travelers = 2
    is_family = False
    booked_destinations_paid_amounts = {}

    def setUp(self):
        self.test_trip = Trip(self.budget,self.travelers,self.is_family)

    def test_init_basic(self):
        self.assertEqual(20000,self.test_trip.budget)
        self.assertEqual(2, self.test_trip.travelers)
        self.assertEqual(False,self.test_trip.is_family)
        self.assertEqual({},self.test_trip.booked_destinations_paid_amounts)

    def test_init_traveler_less_then_one_raises(self):
        with self.assertRaises(ValueError)as e:
            self.test_trip.travelers = 0

        self.assertEqual('At least one traveler is required!',str(e.exception))
        self.assertEqual(2,self.test_trip.travelers)

    def test_init_is_family_returns_false(self):
        t1 = Trip(200,1,True)
        #no need to test 0 travelers, the top case covers it
        self.assertFalse(t1.is_family)

        t2 = Trip(200,1,False)
        self.assertFalse(t2.is_family)

    def test_init_is_family_returns_true(self):
        self.test_trip.travelers = 2
        self.test_trip.is_family = True
        self.assertTrue(self.test_trip.is_family)

        self.test_trip.travelers = 2
        self.test_trip.is_family = False
        self.assertFalse(self.test_trip.is_family)

    def test_book_a_trip_invalid_destination(self):
        result = self.test_trip.book_a_trip('Abu Dhabi')
        self.assertEqual('This destination is not in our offers, please choose a new one!',result)
        self.assertEqual({},self.test_trip.booked_destinations_paid_amounts)

        result = self.test_trip.book_a_trip('Monaco')
        self.assertEqual('This destination is not in our offers, please choose a new one!',result)
        self.assertEqual({},self.test_trip.booked_destinations_paid_amounts)

    def test_book_a_trip_destination_budget_not_enough(self):
        #check if the destination is correct but the budget is low

        self.test_trip.budget = 2000
        result = self.test_trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!',result)
        self.assertEqual(2000,self.test_trip.budget)
        self.assertEqual({},self.test_trip.booked_destinations_paid_amounts)


    def test_book_a_trip_destination_not_family_success(self):
        result = self.test_trip.book_a_trip('New Zealand')
        self.assertEqual('Successfully booked destination New Zealand! Your budget left is 5000.00',result)
        self.assertEqual({'New Zealand':15000},self.test_trip.booked_destinations_paid_amounts)
        self.assertEqual(5000,self.test_trip.budget)


        result = self.test_trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!',result)
        self.assertEqual({'New Zealand':15000},self.test_trip.booked_destinations_paid_amounts)
        self.assertEqual(5000,self.test_trip.budget)



    def test_book_a_trip_destination_is_family_success(self):
        self.test_trip.is_family = True
        result = self.test_trip.book_a_trip('New Zealand')

        self.assertEqual('Successfully booked destination New Zealand! Your budget left is 6500.00', result)
        self.assertEqual({'New Zealand': 13500},self.test_trip.booked_destinations_paid_amounts)
        self.assertEqual(6500,self.test_trip.budget)

        result = self.test_trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!',result)
        self.assertEqual({'New Zealand':13500},self.test_trip.booked_destinations_paid_amounts)
        self.assertEqual(6500,self.test_trip.budget)



    def test_booking_status_no_bookings(self):
        result = self.test_trip.booking_status()
        self.assertEqual(f'No bookings yet. Budget: 20000.00',result)
        self.assertEqual({},self.test_trip.booked_destinations_paid_amounts)
        self.assertEqual(20000, self.test_trip.budget)

    def test_booking_status_has_bookings(self):
        self.test_trip.booked_destinations_paid_amounts = {'New Zealand': 1500,'Australia': 11400}
        result = self.test_trip.booking_status()

        self.assertEqual('Booked Destination: Australia\nPaid Amount: 11400.00\n'
                    'Booked Destination: New Zealand\nPaid Amount: 1500.00\n'
                    'Number of Travelers: 2\nBudget Left: 20000.00',result)




if __name__ == '__main__':
    main()