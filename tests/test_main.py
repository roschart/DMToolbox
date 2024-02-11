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

def test_calculate_attack_roll_ca_out_of_range():
    # Test cases where CA is out of the valid range [-6, 9]
    with pytest.raises(ValueError):
        calculate_attack_roll(-7, 1, "Thief")
    with pytest.raises(ValueError):
        calculate_attack_roll(10, 1, "Cleric")
 