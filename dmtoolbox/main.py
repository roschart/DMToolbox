from typing import Literal

# Alias for the character class type
CharacterClass = Literal[
    "Cleric", "Elf", "Dwarf", "Ranger", "Warrior", "Thief", "Halfling", "Wizard"
]


def calculate_attack_roll(
    monster_ac: int, character_level: int, character_class: CharacterClass
) -> int:
    def calculate_row(character_level: int, character_class: CharacterClass) -> int:
        limits:list[int]
        match character_class:
            case "Cleric" | "Thief":
                limits = [3, 5, 8, 10, 11, 12, 14, 16, 18, 20]
            case "Withard":
                limits = [3, 7, 10, 12, 13, 15, 18, 20, 23, 24]
            case _:
                limits = [2,3,4,5,6,8,9,11,12,13,14,15,16,17,18]
        for i, limit in enumerate(limits):
            if character_level <= limit:
                return i + 1
        return len(limits) + 1

    

    match (monster_ac, character_level, character_class):
        case (_, 0, _):
            return max(2, min(20, 20 - monster_ac))
        case _:
            r = calculate_row(character_level, character_class)
            return max(2, min(20, 20 - monster_ac - r))
