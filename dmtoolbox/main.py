from typing import Literal
from enum import Enum


class CharacterClass(Enum):
    CLERIC = "CLERIC"
    ELF = "ELF"
    DWARF = "DWARF"
    RANGER = "RANGER"
    WARRIOR = "WARRIOR"
    THIEF = "THIEF"
    HALFLING = "HALFLING"
    WIZARD = "WIZARD"
    PALADIN = "PALADIN"


def calculate_pj_attack_roll(
    monster_ac: int, character_level: int, character_class: CharacterClass
) -> int:
    def calculate_row(character_level: int, character_class: CharacterClass) -> int:
        limits: list[int]
        match character_class:
            case CharacterClass.CLERIC | CharacterClass.THIEF:
                limits = [3, 5, 8, 10, 11, 12, 14, 16, 18, 20]
            case CharacterClass.WIZARD:
                limits = [3, 7, 10, 12, 13, 15, 18, 20, 23, 24]
            case _:
                limits = [2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]
        for i, limit in enumerate(limits):
            if character_level <= limit:
                return i + 1
        return len(limits) + 1

    if not (-6 <= monster_ac <= 9):
        raise ValueError("Monster AC must be between -6 and 9.")
    r = 0
    if character_level > 0:
        r = calculate_row(character_level, character_class)
    return max(2, min(20, 20 - monster_ac - r))


def calculate_monster_attack_roll(pj_ac: int, hit_dice: float) -> int:
    limits = [*range(1, 8), *range(9, 22, 2)]
    for i, limit in enumerate(limits):
        if hit_dice <= limit:
            return max(2, min(20, 20 -pj_ac- i - 1))
    raise ValueError(f"Bad values of ac {pj_ac} or hit dice {hit_dice}")
