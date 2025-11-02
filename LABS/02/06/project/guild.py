from project.player import Player

class Guild:
    def __init__(self,name :str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self,player: Player) -> str:
        is_in_guild = any(player.name == p.name for p in self.players)

        if not is_in_guild:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"

            else:
                return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."


    def kick_player(self,player_name: str):
        player = next((p for p in self.players if p.name == player_name),None)

        if player:
            player.guild = "Unaffiliated" or player.guild == self.name
            self.players.remove(player)
            return "Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."


    def guild_info(self):
        info = '\n'.join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n{info}"
