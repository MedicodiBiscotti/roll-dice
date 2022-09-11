import random as rnd


def roll_dice(rolls: int, faces: int) -> list[int]:
    return [rnd.randint(1, faces) for i in range(rolls)]

if __name__ == "__main__":
    print(roll_dice(2, 20))
