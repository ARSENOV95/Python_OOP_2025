from unittest import TestCase,main
from project.soccer_player import SoccerPlayer

class SoccerPlayerTest(TestCase):
    VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def test_init_success(self):
        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        self.assertEqual('George',player.name)
        self.assertEqual(16, player.age)
        self.assertEqual(2, player.goals)
        self.assertEqual('Barcelona', player.team)
        self.assertEqual({}, player.achievements)


    def test_init_name_less_then_five_symbols(self):
        with self.assertRaises(ValueError) as ve:
             player = SoccerPlayer('T',17,0,'Barcelona')
        self.assertEqual("Name should be more than 5 symbols!",str(ve.exception))

        with self.assertRaises(ValueError) as ve:
             player = SoccerPlayer('Test1',17,0,'Barcelona')
        self.assertEqual("Name should be more than 5 symbols!",str(ve.exception))

    def test_init_age_below_16_years(self):
        with self.assertRaises(ValueError) as ve:
            player = SoccerPlayer('George', 15, 0, 'Barcelona')
        self.assertEqual("Players must be at least 16 years of age!",str(ve.exception))

    def test_input_goals_are_negative(self):
        player = SoccerPlayer('George', 16, -1, 'Barcelona')
        self.assertEqual(0,player.goals)

    def test_input_team_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            player = SoccerPlayer('George', 16, -1, 'MAN UTD')
        self.assertEqual(f"Team must be one of the following: {', '.join(self.VALID_TEAMS)}!",str(ve.exception))


    def test_change_team_not_successful(self):
        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        result = player.change_team('MAN UTD')
        self.assertEqual("Invalid team name!",result)
        self.assertEqual('Barcelona',player.team)

    def test_change_team_successful(self):
        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        result = player.change_team('PSG')
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual('PSG', player.team)

        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        result = player.change_team('Barcelona')
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual('Barcelona', player.team)


    def test_add_achievement_if_achievement_already_in_achievements(self):
        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        player.achievements = {'bla':1,'blabla':2}
        player.add_new_achievement('bla')
        self.assertEqual(len(player.achievements),2)
        self.assertEqual({'bla':2,'blabla':2},player.achievements)

    def test_add_achievement_successfull(self):
        player = SoccerPlayer('George', 16, 2, 'Barcelona')
        player.achievements = {'bla': 1, 'blabla': 2}
        player.add_new_achievement('blablabla')

        self.assertEqual(len(player.achievements),3)
        self.assertEqual({'bla': 1, 'blabla': 2,'blablabla':1},player.achievements)



    def test_lt_overloading(self):
        player1 = SoccerPlayer('George', 16, 2, 'Barcelona')
        player2 = SoccerPlayer('Patar69', 18, 3, 'Barcelona')

        self.assertEqual(player1 < player2,'Patar69 is a top goal scorer! S/he scored more than George.')
        self.assertEqual(player2 < player1,f"Patar69 is a better goal scorer than George.")

if __name__ == '__main_':
    main()

