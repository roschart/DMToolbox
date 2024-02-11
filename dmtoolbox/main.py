from typing import Literal

# Alias for the character class type
CharacterClass = Literal[
    "Cleric", "Elf", "Dwarf", "Ranger", "Warrior", "Thief", "Halfling"
]


def calculate_attack_roll(
    monster_ac: int, character_level: int, character_class: CharacterClass
) -> int:
    match (monster_ac, character_level, character_class):
        case (_, 0, _) :
            return 0
        case _:
            raise ValueError("Calculated_attac_roll not implemented")
