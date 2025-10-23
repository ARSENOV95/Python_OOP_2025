from project.pokemon import Pokemon

class Trainer:
    def __init__(self,name:str):
        self.name = name
        self.pokemons: list[Pokemon] = []
        
        
    def add_pokemon(self,curr_pokemon: Pokemon) -> str:
        is_caught = any(p for p in self.pokemons if p == curr_pokemon)

        if is_caught:
            return "This pokemon is already caught"
        
        self.pokemons.append(curr_pokemon)
        return f"Caught {curr_pokemon.pokemon_details()}"
        
    def release_pokemon(self,pokemon_name: str):
        is_released = next((p for p in self.pokemons if p.name == pokemon_name), None)

        if is_released:
                self.pokemons.remove(is_released)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"
        

    def trainer_data(self):
        result = ''
        result += f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        for p in self.pokemons:
            result += f'- {Pokemon.pokemon_details(p)}\n'
        
        return result
            
