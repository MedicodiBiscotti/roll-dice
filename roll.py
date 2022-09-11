import argparse
import random as rnd


def roll_dice(rolls: int, faces: int) -> list[int]:
    return [rnd.randint(1, faces) for i in range(rolls)]

def main(rolls: int, faces: int) -> None:
    print(roll_dice(rolls, faces))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rolls dice")
    parser.add_argument('rolls', type=int, help="Number of dice to roll")
    parser.add_argument('faces', type=int, help="Number of faces/sides on the die")
    args = parser.parse_args()
    main(args.rolls, args.faces)
