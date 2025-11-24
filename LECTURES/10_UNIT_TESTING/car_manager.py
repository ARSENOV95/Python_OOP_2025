class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

#car = Car("a", "b", 1, 4)
#car.make = ""
#print(car)

from unittest import TestCase,main

class CarTests(TestCase):
    def setUp(self):
        self.car = Car('Honda','Accord',5.6,65)
        self.car.fuel_amount = 0

    def test_car_init(self):
        car = Car('Toyota','Prius',3,60)

        self.assertEqual('Toyota',car.make)
        self.assertEqual('Prius',car.model)
        self.assertEqual(3,car.fuel_consumption)
        self.assertEqual(60,car.fuel_capacity)
        self.assertEqual(0,car.fuel_amount)


    def test_car_make_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!",str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!",str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_car_model_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_fuel_consumption_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!",str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!",str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_fuel_capacity_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_car_fuel_amount_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -3
        self.assertEqual("Fuel amount cannot be negative!",str(ex.exception))

    def test_car_refuel_raises_error(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_car_refuel(self):
        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(70)

        self.assertEqual(65,self.car.fuel_amount)


    def test_car_drive_raises_error(self):
        self.car.refuel(10)

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(10, self.car.fuel_amount)


        with self.assertRaises(Exception) as ex:
            self.car.drive(300)
        self.assertEqual("You don't have enough fuel to drive!",str(ex.exception))

    def test_car_drive(self):
        self.car.refuel(10)

        self.assertEqual('Honda', self.car.make)
        self.assertEqual('Accord', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(10, self.car.fuel_amount)


        self.assertEqual(9.44,self.car.fuel_amount)

if __name__ == '__main__':
    main()