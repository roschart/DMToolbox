# dmtoolbox/__main__.py
import argparse
from .main import calculate_monster_attack_roll, calculate_pj_attack_roll, CharacterClass

import argparse


def main():

    parser = argparse.ArgumentParser(description="DMToolbox CLI")
    subparsers = parser.add_subparsers(
        dest="command", help="Operation command", required=True
    )

    # attack subparsers
    parser_attack = subparsers.add_parser("attack", help="Manage attacks")
    attack_subparsers = parser_attack.add_subparsers(
        dest="attack_type", help="Type of attack", required=True
    )
    # Subparser for "attack pj"
    parser_pj = attack_subparsers.add_parser("pj", help="Player character attack")
    parser_pj.add_argument(
        "-c",
        "--character-class",
        type=CharacterClass,
        choices=list(CharacterClass),
        required=True,
        help="Character class",
    )
    parser_pj.add_argument("-a", "--ac", type=int, required=True, help="Monster AC")
    parser_pj.add_argument(
        "-l", "--level", type=int, required=True, help="Character level"
    )

    # Subparser para "attack monster"
    parser_monster = attack_subparsers.add_parser("monster", help="Monster attack")
    parser_monster.add_argument(
        "-a", "--ac", type=int, required=True, help="Player character AC"
    )
    parser_monster.add_argument(
        "-d", "--hit-dice", type=float, required=True, help="Monster hit dice"
    )

    # Parser para el comando "battle"
    subparsers.add_parser("battle", help="Battle command not implemented")

    args = parser.parse_args()

    # Lógica para manejar los comandos
    if args.command == "attack":
        if args.attack_type == "pj":
            result = calculate_pj_attack_roll(args.ac, args.level, args.character_class)
            print(f"PJ Attack roll needed: {result}")
        elif args.attack_type == "monster":
            result= calculate_monster_attack_roll(args.ac, args.hit_dice)
            print(f"Monster Attack roll needed: {result}")
    elif args.command == "battle":
        print("Battle command not implemented")


if __name__ == "__main__":
    main()
