import pytest

from dmtoolbox.main import calculate_attack_roll

def test_calculate_attack_roll_success_cases():
    # CA, level, class, expected result
    test_cases = [
        (6, 0, "Any", 14),
        (-4, 1, "Thief", 20),
        (-4, 13, "Cleric", 17),
        (9, 4, "Elf", 8),
    ]

    for ca, level, char_class, expected in test_cases:
        assert calculate_attack_roll(ca, level, char_class) == expected

@pytest.mark.parametrize("monster_ac, character_level, character_class", [
    (-7, 1, "Thief"),  # CA fuera de rango
    (10, 1, "Cleric"),  # CA fuera de rango
])
def test_calculate_attack_roll_ca_out_of_range(monster_ac, character_level, character_class):
    with pytest.raises(ValueError):
        calculate_attack_roll(monster_ac, character_level, character_class)

 