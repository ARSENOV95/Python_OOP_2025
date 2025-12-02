from unittest import TestCase,main
from project.climbing_robot import ClimbingRobot

class ClimbingRobotTest(TestCase):
    category = 'Mountain'
    part_type = 'test_part'
    capacity = 10
    memory = 128
    installed_software = []

    def setUp(self):
        self.test_robo = ClimbingRobot(self.category,self.part_type,self.capacity,self.memory)


    def test_init_basic(self):
        self.assertEqual('Mountain',self.test_robo.category)
        self.assertEqual('test_part', self.test_robo.part_type)
        self.assertEqual(10, self.test_robo.capacity)
        self.assertEqual(128, self.test_robo.memory)
        self.assertEqual([], self.test_robo.installed_software)

    def test_validate_category(self):
        self.assertIn(self.category, ClimbingRobot.ALLOWED_CATEGORIES)


    def test_init_category_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robo.category = 'Test'
        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']",str(ve.exception))
        self.assertEqual("Mountain",self.test_robo.category)


    def test_init_used_capacity(self):
        self.installed_software = [{'ABC':2}]
        result =


    def test_init_available_capacity(self):
        pass


if __name__ == '__main__':
    main()