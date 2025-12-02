from unittest import TestCase,main

from project.gallery import Gallery

class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("Valid","Sofia",20,False)


    def test_init(self):
        self.assertEqual("Valid",self.gallery.gallery_name)
        self.assertEqual('Sofia',self.gallery.city)
        self.assertEqual(20,self.gallery.area_sq_m)
        self.assertFalse(self.gallery.open_to_public)


    def test_name_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("","Sofia",10.0,False)
        self.assertEqual("Gallery name can contain letters and digits only!",str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("sR4!$A", "Sofia", 10.0, False)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_invalid_city_name(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Valid","!Sofia",10.0,False)
        self.assertEqual("City name must start with a letter!",str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "4Sofia", 10.0, False)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "", 10.0, False)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_invalid_area_raises(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Valid","Sofia",0.0,False)
        self.assertEqual("Gallery area must be a positive number!",str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid","Sofia",-0.9,False)
        self.assertEqual("Gallery area must be a positive number!",str(ex.exception))

    def test_add_exhibition_sucCess(self):
        self.gallery.exhibitions = {"A":2023}
        result = self.gallery.add_exhibition("B",2002)
        self.assertEqual(f'Exhibition "B" added for the year 2002.',result)
        self.assertEqual({"A":2023,"B":2002},self.gallery.exhibitions)

    def test_add_exhibition_exists(self):
        self.gallery.exhibitions = {"A":2023}
        result = self.gallery.add_exhibition("A",2023)
        self.assertEqual(f'Exhibition "A" already exists.',result)
        self.assertEqual({"A":2023},self.gallery.exhibitions)




    def test_remove_exhibition_does_not_exist(self):
        self.gallery.exhibitions = {"A": 2023}
        result = self.gallery.remove_exhibition("B")
        self.assertEqual(f'Exhibition "B" not found.',result)
        self.assertEqual({"A": 2023},self.gallery.exhibitions)

    def test_remove_exhibition_success(self):
        self.gallery.exhibitions = {"A":2023,"B":2002}
        result = self.gallery.remove_exhibition("B")
        self.assertEqual(f'Exhibition "B" removed.',result)
        self.assertEqual({"A":2023},self.gallery.exhibitions)

    def test_list_exhibitions_open(self):
        self.gallery.open_to_public = True
        self.gallery.exhibitions = {"A":2023,"B":2002}
        result = self.gallery.list_exhibitions()

        self.assertEqual(f"A: 2023\nB: 2002",result)

    def test_list_exhibitions_closed(self):
        self.gallery.exhibitions = {"A": 2023, "B": 2002}
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(f'Gallery Valid is currently closed for public! Check for updates later on.',result)
        self.assertEqual({"A": 2023, "B": 2002},self.gallery.exhibitions)

if __name__ == '__main__':
    main()

