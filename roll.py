import argparse
import random as rnd
from typing import Callable


def roll_dice(rolls: int, faces: int) -> list[int]:
    return [rnd.randint(1, faces) for i in range(rolls)]

def main(rolls: int, faces: int, op: Callable) -> None:
    print(roll_dice(rolls, faces))

def sum_rolls(rolls: int, faces: int, results: list[int]) -> None:
    sum_result = sum(results)
    expected_avg = (faces / 2 + 0.5) * rolls

def advantage():
    pass

def disadvantage():
    pass

def raw():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rolls dice")
    parser.add_argument('rolls', type=int, nargs='?', default=1, help="Number of dice to roll (default: 1)")
    parser.add_argument('faces', type=int, nargs='?', default=20, help="Number of faces/sides on the die (default: 20)")

    arg_group = parser.add_mutually_exclusive_group()
    arg_group.add_argument('-s', '--sum',
        dest='op', action='store_const', const=sum_rolls, default=sum_rolls,
        help="Sums the result of the rolls (default)")

    arg_group.add_argument('-a', '--advantage',# '--adv',
        dest='op', action='store_const', const=advantage,
        help="Roll with advantage, i.e. take the highest of the rolls")

    arg_group.add_argument('-d', '--disadvantage',# '--dis',
        dest='op', action='store_const', const=disadvantage,
        help="Roll with disadvantage, i.e. take the lowest of the rolls")

    arg_group.add_argument('-r', '--raw',
        dest='op', action='store_const', const=raw,
        help="Returns the resulting rolls in a list as is")

    args = parser.parse_args()

    # sum is True by default if nothing else is specified
    # if not any([args.sum, args.advantage, args.disadvantage]):
    #     args.sum = True
    print(args)
    
    main(args.rolls, args.faces)
