class SteamUser:
    def __init__(self,username :str,games :list):
        self.username = username
        self.games = games
        self.played_hours = 0
        
    def play(self,game,hours):
        in_list = any(x for x in self.games if x == game)
        
        if in_list:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        
        return  f"{game} is not in library"
        
    
    def buy_game(self,game):
        in_list = any(x for x in self.games if x == game)
        
        if not in_list:
            self.games.append(game)
            return f"{self.username} bought {game}"
        
        return f"{game} is already in your library"
        
    def status(self):
        games_count = len(self.games)
        return f"{self.username} has {games_count} games. Total play time: {self.played_hours}"
    
 
    
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())