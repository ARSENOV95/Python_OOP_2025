from project.pokemon import Pokemon

class Trainer:
    def __init__(self,name:str):
        self.name = name
        self.pokemon_coll = list()
        
        
    def add_pokemon(self,curr_pokemon: Pokemon):
        is_caught = any(p for p in self.pokemon_coll if p == curr_pokemon)
        if is_caught:
            return "This pokemon is already caught"
        
        self.pokemon_coll.append(curr_pokemon)
        return f"Caught {Pokemon.pokemon_details(curr_pokemon)}"
        
    def release_pokemon(self,pokemon_name: str):
        for p in self.pokemon_coll:
            if p.name == pokemon_name:
                self.pokemon_coll.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"
        

    
    def trainer_data(self):
        result = ''
        result += f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon_coll)}\n'
        for p in self.pokemon_coll:
            result += f'- {Pokemon.pokemon_details(p)}\n'
        
        return result
            
