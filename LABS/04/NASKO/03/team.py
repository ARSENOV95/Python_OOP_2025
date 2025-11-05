from project.player import Player

class Team:
    from project.player import Player

    class Team:
        def __init__(self, name: str, rating: int):
            self.__name = name
            self.__rating = rating
            self.__players: list[Player] = []

        def add_player(self, player: Player) -> str:
            if player in self.players:
                return f"Player {player.name} has already joined"
            self.players.append(player)
            return f"Player {player.name} joined team {self.__name}"

        def remove_player(self, player_name: str) -> str | Player:
            player = next((p for p in self.players if p.name == player_name), None)

            if player:
                self.players.remove(player)
                return player
            return f"Player {player_name} not found"
