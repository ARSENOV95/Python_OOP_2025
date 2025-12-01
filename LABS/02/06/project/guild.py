from project.player import Player

class Guild:
    def __init__(self,name :str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self,player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != self.name and  player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"


    def kick_player(self,player_name: str):
        player = next((p for p in self.players if p.name == player_name),None)

        if player is None:
            return f"Player {player_name} is not in the guild."

        player.guild = "Unaffiliated"
        self.players.remove(player)
        return f"Player {player.name} has been removed from the guild."


    def guild_info(self):
        info = f"Guild: {self.name}\n"
        return info + '\n'.join(p.player_info() for p in self.players)

