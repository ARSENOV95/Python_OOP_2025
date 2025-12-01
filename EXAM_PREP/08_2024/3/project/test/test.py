from unittest import TestCase,main

from project.furniture import Furniture

class FurnitureTest(TestCase):
    model:str = 'Test'
    price:float = 1.0
    dimensions:tuple[int,int,int] = (1,1,1)
    in_stock:bool = True
    weight:float = None

    def setUp(self):
        self.furniture = Furniture(self.model
                                   ,self.price
                                   ,self.dimensions
                                   ,self.in_stock
                                   ,self.weight)


    def test_input_success(self):
        self.assertEqual('Test',self.furniture.model)
        self.assertEqual(1.0,self.furniture.price)
        self.assertEqual((1,1,1),self.furniture.dimensions)
        self.assertTrue('True,',self.furniture.in_stock)
        self.assertIsNone(self.furniture.weight)


    def test_model_init_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ''
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.",str(ex.exception))
        self.assertEqual('Test',self.furniture.model)

        with self.assertRaises(ValueError) as ex:
            self.furniture.model = '' * 50
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.",str(ex.exception))
        self.assertEqual('Test',self.furniture.model)


        with self.assertRaises(ValueError) as ex:
            test_model = 'a'* 51
            self.furniture.model = test_model
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.",str(ex.exception))
        self.assertEqual('Test',self.furniture.model)


    def test_price_init_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -0.9
        self.assertEqual("Price must be a non-negative number.",str(ex.exception))
        self.assertEqual(1.0,self.furniture.price)



    def test_dimensions_init_not_enough_values_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (1,1)
        self.assertEqual("Dimensions tuple must contain 3 integers.",str(ex.exception))
        self.assertEqual((1,1,1),self.furniture.dimensions)

        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (1,1,1,1)
        self.assertEqual("Dimensions tuple must contain 3 integers.",str(ex.exception))
        self.assertEqual((1,1,1),self.furniture.dimensions)


    def test_dimensions_init_negative_values_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (1,-1,1)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.",str(ex.exception))
        self.assertEqual((1,1,1),self.furniture.dimensions)

        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (1,0,1)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.",str(ex.exception))
        self.assertEqual((1,1,1),self.furniture.dimensions)

        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (0,0,0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.",str(ex.exception))
        self.assertEqual((1,1,1),self.furniture.dimensions)



    def text_weight_zero_or_negative_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = 0.0
        self.assertEqual("Weight must be greater than zero.",str(ex.exception))
        self.assertEqual(None,self.furniture.weight)

        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -0.9
        self.assertEqual("Weight must be greater than zero.",str(ex.exception))
        self.assertEqual(None, self.furniture.weight)

    def test_get_available_status(self):
        self.furniture.in_stock = True
        self.assertTrue(self.furniture.in_stock)
        result = self.furniture.get_available_status()
        self.assertEqual(f"Model: Test is currently in stock.",result)

        self.furniture.in_stock = False
        self.assertFalse(self.furniture.in_stock)
        result = self.furniture.get_available_status()
        self.assertEqual(f"Model: Test is currently unavailable.",result)

    def test_get_specifications(self):
        result = self.furniture.get_specifications()
        self.assertEqual(f"Model: Test has the following dimensions: 1mm x 1mm x 1mm and weighs: N/A",result)


        self.furniture.weight = 1.0
        result = self.furniture.get_specifications()
        self.assertEqual(f"Model: Test has the following dimensions: 1mm x 1mm x 1mm and weighs: 1.0",result)


if __name__ == '__main__':
    main()