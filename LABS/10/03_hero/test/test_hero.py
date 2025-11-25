from unittest import TestCase,main
from project.hero import Hero

class HeroTest(TestCase):
    def setUp(self):
        self.username = 'Test name'
        self.level = 5
        self.health = 16.8
        self.damage = 9.4


        self.test_hero = Hero(self.username,self.level,self.health,self.damage)


    def test_init_type(self):
        self.assertIsInstance(self.test_hero.username,str)
        self.assertIsInstance(self.test_hero.level, int)
        self.assertIsInstance(self.test_hero.health, float)
        self.assertIsInstance(self.test_hero.damage, float)

    def test_init(self):
        self.assertEqual(self.username,self.test_hero.username)
        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(self.health, self.test_hero.health)
        self.assertEqual(self.damage, self.test_hero.damage)


    def test_enemy_hero_same_as_hero(self):
        enemy = Hero(self.username,self.level,self.health,self.damage)

        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(enemy)

        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_hero_health_not_enough(self):
        self.test_hero.health = 0
        enemy = Hero("Enemy", self.level, self.health,self.damage)
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

        self.test_hero.health = - 1
        enemy = Hero("Enemy",self.level,self.health,self.damage)
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

    def test_enemy_health_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)

        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest",str(ex.exception))

        enemy = Hero("Enemy", self.level, -1, self.damage)


        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest",str(ex.exception))

    def test_battle_ends_in_draw(self):
        enemy = Hero("Enemy", self.level, self.health,self.damage)

        result = self.test_hero.battle(enemy)

        self.assertEqual("Draw",result)
        self.assertEqual(self.level,self.test_hero.level)
        self.assertEqual(-30.2,self.test_hero.health)
        self.assertEqual(self.damage,self.test_hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Enemy", 1, 1,1)
        result = self.test_hero.battle(enemy)
        self.assertEqual(6,self.test_hero.level)
        self.assertEqual(20.8, self.test_hero.health)
        self.assertEqual(14.4, self.test_hero.damage)
        self.assertEqual("You win",result)

    def test_hero_loses(self):
        self.test_hero.health = 10
        self.test_hero.damage  = 10

        enemy = Hero("Enemy",100,100,100)

        result = self.test_hero.battle(enemy)

        self.assertEqual(101,enemy.level)
        self.assertEqual(55,enemy.health)
        self.assertEqual(105,enemy.damage)
        self.assertEqual("You lose",result)



if __name__ == "__main__":
    main()