class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase,main

class ListTest(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(100,1,12)


    def test_init(self):
        i  = IntegerList(1,'5',10.7,6)

        self.assertEqual([1,6],i.get_data())
                            #exopected result to be a list with [1,6]

        self.assertEqual([1,6],i._IntegerList__data)
        # we check the result fo the input but we need to check if __data exists via the mangled class prop


    def test_add_element(self):
        self.assertEqual([100,1,12],self.integer_list.get_data())

        with self.assertRaises(Exception) as ex:
            self.integer_list.add('A')
        self.assertEqual("Element is not Integer",str(ex.exception))

        self.assertEqual([100,1,12],self.integer_list.get_data())

        with self.assertRaises(Exception) as ex:
            self.integer_list.add(1.7)
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())
        result = self.integer_list.add(7)

        self.assertEqual([100, 1, 12,7], self.integer_list.get_data())
        self.assertEqual([100, 1, 12,7], result) # проверкадал и раболитло в дължината

    def test_remove_index_not_a_valid_index_raises(self):
        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        with self.assertRaises(Exception) as ex:
            self.integer_list.remove_index(3)
        self.assertEqual("Index is out of range",str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        with self.assertRaises(Exception) as ex:
            self.integer_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

    def test_remove_index(self):
        self.assertEqual([100,1,12],self.integer_list.get_data())

        result =self.integer_list.remove_index(1)
        #remove middle index to insure remove not pop was used i nthe code
        self.assertEqual([100,12],self.integer_list.get_data())
        self.assertEqual(1,result)

    def test_get_invalid_index_raises(self):
        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(3)
        self.assertEqual("Index is out of range",str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

    def test_get_insert_raise(self):
        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(3,1)
        self.assertEqual("Index is out of range",str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())


        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(4,1)
        self.assertEqual("Index is out of range",str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

    def test_insert_invalid_element_type_raises(self):

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1,2.3)
        self.assertEqual("Element is not Integer",str(ex.exception))

        self.assertEqual([100, 1, 12], self.integer_list.get_data())

    def test_insert(self):
        self.assertEqual([100,1,12],self.integer_list.get_data())
        result = self.integer_list.insert(0,300)

        self.assertEqual([300,100,1,12],self.integer_list.get_data())
        self.assertIsNone(result)

    def test_get_biggest(self):
        self.integer_list.insert(0,30)
        self.assertEqual([30,100,1,12],self.integer_list.get_data())

        result = self.integer_list.get_biggest()

        self.assertEqual(100,self.integer_list.get_biggest())
        self.assertEqual(100,result)

    def test_get_index(self):
        self.assertEqual([100, 1, 12], self.integer_list.get_data())

        result = self.integer_list.get_index(1)

        self.assertEqual(1,result)



if __name__ == "__main__":
    main()