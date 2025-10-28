from project.player import Player
from project.guild import  Guild

player = Player("Pesho", 90, 90)
print(player.add_skill("A", 3))
print(player.add_skill("A", 3))
print(player.player_info())
guild = Guild("GGXrd")
print(guild.assign_player(player))
print(guild.assign_player(player))
