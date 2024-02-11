import pytest

from dmtoolbox.main import calculate_attack_roll

@pytest.mark.parametrize("monster_ac, character_level, character_class, expected", [
    (6, 0, "Any", 14),
    (-4, 1, "Thief", 20),
    (0, 1, "Thief", 19),
    (-4, 13, "Cleric", 17),
    (9, 20, "Cleric", 2),
    (9, 15, "Cleric", 3),
    (9, 22, "Cleric", 2),
    (9, 4, "Elf", 8),
    (5,11,"Withard",11),
    (0,23,"Paladin",4)
])
def test_calculate_attack_roll_success_cases(monster_ac, character_level, character_class, expected):
    assert calculate_attack_roll(monster_ac, character_level, character_class) == expected
@pytest.mark.parametrize("monster_ac, character_level, character_class", [
    (-7, 1, "Thief"),  # CA fuera de rango
    (10, 1, "Cleric"),  # CA fuera de rango
])
def test_calculate_attack_roll_ca_out_of_range(monster_ac, character_level, character_class):
    with pytest.raises(ValueError):
        calculate_attack_roll(monster_ac, character_level, character_class)

 