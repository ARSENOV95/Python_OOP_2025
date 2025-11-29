from project.battle_manager import BattleManager

battle_manager = BattleManager()

print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()

print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
print()

