from project.gallery import Gallery
from unittest import TestCase,main


class GalleryTest(TestCase):
    gallery_name = 'DuDuDuDUU'
    city = 'Max Verstappen'
    area_sq_m = 20.5
    open_to_public = False
    exhibition = {}


    def setUp(self):
        self.gallery = Gallery(self.gallery_name,self.city,self.area_sq_m,self.open_to_public)

    def test_attribute_types(self):
        self.assertIsInstance(self.gallery.gallery_name,str)
        self.assertIsInstance(self.gallery.city,str)
        self.assertIsInstance(self.gallery.area_sq_m,float)
        self.assertIsInstance(self.gallery.open_to_public,bool)
        self.assertIsInstance(self.gallery.exhibitions,dict)

    def test_init_successful(self):
        self.assertEqual(self.gallery_name,self.gallery.gallery_name)
        self.assertEqual(self.city,self.gallery.city)
        self.assertEqual(self.area_sq_m, self.gallery.area_sq_m)
        self.assertEqual(self.open_to_public, self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)


    def test_input_name_error_letters_and_digits_only(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = 'No Miki No!'
        self.assertEqual("Gallery name can contain letters and digits only!",str(ve.exception))

    def test_input_city_name_error_name_must_start_with_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = '2BoxBox'
        self.assertEqual("City name must start with a letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.gallery.city = ''
        self.assertEqual("City name must start with a letter!", str(ve.exception))

    def test_input_area_negative_number_error(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!",str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m =  -1
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

        self.assertEqual(self.area_sq_m,self.gallery.area_sq_m)

    def test_add_exhibition_exhibition_already_in_dict(self):
        self.gallery.exhibitions = {'A':1,'B':2}
        result = self.gallery.add_exhibition('A',1)

        self.assertEqual('Exhibition "A" already exists.',result)
        self.assertEqual({'A':1,'B':2},self.gallery.exhibitions)

    def test_add_exhibition_exhibition_successfully_added(self):
        self.gallery.exhibitions = {'A': 1, 'B': 2}
        result = self.gallery.add_exhibition('C', 3)

        self.assertEqual('Exhibition "C" added for the year 3.',result)
        self.assertEqual({'A':1,'B':2,'C':3},self.gallery.exhibitions)

    def test_remove_exhibition_exception_not_in_list(self):
        self.gallery.exhibitions = {'A': 1, 'B': 2}

        result = self.gallery.remove_exhibition('C')

        self.assertEqual('Exhibition "C" not found.',result)
        self.assertEqual({'A': 1, 'B': 2},self.gallery.exhibitions)

    def test_remove_exhibition_successfully(self):
        self.gallery.exhibitions = {'A': 1, 'B': 2,'C':3}
        result = self.gallery.remove_exhibition('C')

        self.assertEqual('Exhibition "C" removed.',result)
        self.assertEqual({'A': 1, 'B': 2},self.gallery.exhibitions)

    def test_remove_exhibition_closed_for_public(self):
        self.assertFalse(self.gallery.open_to_public)
        result = self.gallery.list_exhibitions()
        self.assertEqual(f'Gallery DuDuDuDUU is currently closed for public! Check for updates later on.',result)

        self.assertFalse(self.gallery.open_to_public)

    def test_remove_exhibition_opened_for_public(self):
        pass



if __name__ == "__main__":
    main()