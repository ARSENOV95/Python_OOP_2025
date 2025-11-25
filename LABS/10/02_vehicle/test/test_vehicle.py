from unittest import TestCase,main
from project.vehicle import Vehicle



class VehicleTest(TestCase):
    fuel = 4.5
    horse_power = 112.5
    def setUp(self):
        self.test_vehicle = Vehicle(self.fuel,self.horse_power)

    #check input types
    def test_class_attributes_type(self):
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION,float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity,float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)

    #heck input valuies
    def test_init(self):
        self.assertEqual(self.fuel,self.test_vehicle.fuel)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25,self.test_vehicle.fuel_consumption)


    def test_drive(self):
        self.test_vehicle.drive(2)
        self.assertEqual(2,self.test_vehicle.fuel)


    def test_drive_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(5)
        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_refuel_success(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(2.3)
        self.assertEqual(3.3,self.test_vehicle.fuel)

    def test_refuel_error(self):
        self.test_vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(8.5)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_str(self):
        result = self.test_vehicle.fuel = 1.75

        expected = "The vehicle has 112.5 horse power with 1.75 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected,str(self.test_vehicle))

if __name__ == '__main__':
    main()