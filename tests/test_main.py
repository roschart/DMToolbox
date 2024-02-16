import pytest

from dmtoolbox.main import calculate_attack_roll, CharacterClass as CC


@pytest.mark.parametrize(
    "monster_ac, character_level, character_class, expected",
    [
        (6, 0, CC.WARRIOR, 14),
        (-4, 1, CC.THIEF, 20),
        (0, 1, CC.THIEF, 19),
        (-4, 13, CC.CLERIC, 17),
        (9, 20, CC.CLERIC, 2),
        (9, 15, CC.CLERIC, 3),
        (9, 22, CC.CLERIC, 2),
        (9, 4, CC.ELF, 8),
        (5, 11, CC.WIZARD, 11),
        (0, 23, CC.PALADIN, 4),
    ],
)
def test_calculate_attack_roll_success_cases(
    monster_ac: int, character_level: int, character_class: CC, expected: int
):
    assert (
        calculate_attack_roll(monster_ac, character_level, character_class) == expected
    )


@pytest.mark.parametrize(
    "monster_ac, character_level, character_class",
    [
        (-7, 1, CC.THIEF),  # CA fuera de rango
        (10, 1, CC.CLERIC),  # CA fuera de rango
    ],
)
def test_calculate_attack_roll_ca_out_of_range(
    monster_ac, character_level, character_class
):
    with pytest.raises(ValueError):
        calculate_attack_roll(monster_ac, character_level, character_class)
