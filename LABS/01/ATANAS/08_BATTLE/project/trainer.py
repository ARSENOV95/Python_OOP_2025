from  project.pokemon import Pokemon #from the project path import the Pokemon class from pokemon.py

class Trainer:
    def __init__(self,name :str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self,pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self,pokemon_name :str) -> str:
        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name),None) #finds the first object in a list and breakes the loop if its not found it returns None as defoult value

        if pokemon_to_release:
            return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name},Pokemon count {len(self.pokemons)}"]
        for pokemon in self.pokemons:
            result.append(f'- {pokemon.pokemon_details()}')

        return  '\n'.join(result)
