class Player:
    def __init__(self,name :str,hp :int,mp :int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills:dict[str,int]= {}
        self.guild = 'Unaffiliated'

    def add_skill(self,skill_name :str, mana_cost :int):
        if not self.skills.get(skill_name):
            self.skills[skill_name] = mana_cost
            return  f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        info = '\n'.join([f'==={skill} - {mana}' for skill,mana in self.skills.items()])
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{info}"

