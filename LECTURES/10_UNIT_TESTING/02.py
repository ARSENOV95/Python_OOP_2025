class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0


    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False

from unittest import  TestCase,main

class CatTests(TestCase):
    def setUp(self):
        self.c = Cat('Mittens')
        self.c.fed = False
        self.c.sleepy = False
        self.c.size = 0



    def test_cat_size_increase(self):
        c_c = self.c
        expected_size = c_c.size + 1

        c_c.eat()

        result = c_c.size

        self.assertEqual(expected_size,result)
        self.assertEqual(True,c_c.fed)
        self.assertEqual(True,c_c.sleepy)

        with self.assertRaises(Exception) as ex:
            c_c.eat()
        self.assertEqual('Already fed.', str(ex.exception))


    def test_cat_cannot_sleep(self):
        c_c = self.c
        c_c.fed = False
        c_c.sleepy = False

        with self.assertRaises(Exception) as ex:
            c_c.sleep()
        self.assertEqual('Cannot sleep while hungry',str(ex.exception))



    def test_is_not_sleepy(self):
        c_c = self.c
        c_c.fed = True
        c_c.sleepy = True


        c_c.sleep()

        self.assertEqual(False,c_c.sleepy)



if __name__ == '__main__':
    main()