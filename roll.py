import argparse
import random as rnd
from typing import Callable

from modules.utils import separater_line


def roll_dice(rolls: int, faces: int) -> list[int]:
    return [rnd.randint(1, faces) for i in range(rolls)]

def sum_rolls(rolls: int, faces: int, modifier: int) -> None:
    results = roll_dice(rolls, faces)
    sum_result = sum(results) + modifier
    expected_avg = (faces / 2 + 0.5) * rolls + modifier
    return (results, sum_result, expected_avg)

def advantage(rolls: int, faces: int, modifier: int):
    results = roll_dice(rolls, faces)
    max_result = max(results) + modifier
    expected_avg = faces * rolls / (rolls + 1) + 0.5 + modifier     # thank you, Matt Parker # m / (m + 1) * n + 0.5
    return (results, max_result, expected_avg)

def disadvantage(rolls: int, faces: int, modifier: int):
    results = roll_dice(rolls, faces)
    min_result = min(results) + modifier
    expected_avg = faces / (rolls + 1) + 0.5 + modifier     # thank you, Matt Parker # 1 / (m + 1) * n + 0.5
    return (results, min_result, expected_avg)

def raw(rolls: int, faces: int):
    return roll_dice(rolls, faces)

def main(rolls: int, faces: int, op: Callable, modifier: int) -> None:
    if op is raw:
        print(op(rolls, faces))
        return
    
    # adjust for advantage and disadvantage
    if op in [advantage, disadvantage]:
        rolls = max(2, rolls)
    
    # pluralize faces if there are multiple rolls.
    # f-string doesn't allow backslashes so you have to either define the desired string as a variable, or use docstring
    intro_str = f"""Rolling {rolls} d{faces}{"'s"[:2*rolls^2]}{f" with a modifier of {modifier}" if modifier else ""}"""
    print(intro_str)
    print(separater_line(len(intro_str), middle=['Good luck', 'GL']))

    raw_results, result, expected_avg = op(rolls, faces, modifier)
    # TODO consider using inflect for joining list
    print("You rolled: " + ', '.join(map(str, raw_results)))        # all this just to get rid of the brackets. perhaps unwarranted.
    print(f"Result: {result}")
    print(f"With an expected value of {round(expected_avg, 2)}")    # val:.2f will have trailing zeros. :.4g won't but converts to scientific notation if needed.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="rolls dice")
    parser.add_argument('rolls', type=int, nargs='?', default=1, help="number of dice to roll (default: 1)")
    parser.add_argument('faces', type=int, nargs='?', default=20, help="number of faces/sides on the die (default: 20)")
    parser.add_argument('-m', '--modifier', type=int, default=0, help="modifier to add to the result")

    arg_group = parser.add_mutually_exclusive_group()
    arg_group.add_argument('-s', '--sum',
        dest='op', action='store_const', const=sum_rolls, default=sum_rolls,
        help="sums the result of the rolls (default)")

    arg_group.add_argument('-a', '--advantage',# '--adv',
        dest='op', action='store_const', const=advantage,
        help="roll with advantage, i.e. take the highest of the rolls")

    arg_group.add_argument('-d', '--disadvantage',# '--dis',
        dest='op', action='store_const', const=disadvantage,
        help="roll with disadvantage, i.e. take the lowest of the rolls")

    arg_group.add_argument('-r', '--raw',
        dest='op', action='store_const', const=raw,
        help="returns the resulting rolls in a list as is")

    args = parser.parse_args()

    # sum is True by default if nothing else is specified
    # if not any([args.sum, args.advantage, args.disadvantage]):
    #     args.sum = True
    # print(args)
    
    main(args.rolls, args.faces, args.op, args.modifier)
