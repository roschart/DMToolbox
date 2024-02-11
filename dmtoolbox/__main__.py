# dmtoolbox/__main__.py
import argparse
from .main import calculate_attack_roll

def main():
    parser = argparse.ArgumentParser(description="DMToolbox Command Line Interface")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Define subcomando "attack"
    parser_attack = subparsers.add_parser("attack", help="Calculate attack roll")
    parser_attack.add_argument("--character-class", required=True, help="Character class")
    parser_attack.add_argument("--ac", type=int, required=True, help="Monster AC")
    parser_attack.add_argument("--level", type=int, required=True, help="Character level")
    
    args = parser.parse_args()

    if args.command == "attack":
        result = calculate_attack_roll(args.ac, args.level, args.character_class)
        print(f"Attack roll needed: {result}")

if __name__ == "__main__":
    main()
