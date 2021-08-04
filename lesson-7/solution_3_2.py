import random


def can_queens_beat_each_other(first_queen: dict, second_queen: dict) -> bool:
    # Both on the same column
    if first_queen["x"] == second_queen["x"]:
        return True

    # Both on the same row
    if first_queen["y"] == second_queen["y"]:
        return True

    # Both on the same diagonal
    if abs(first_queen["x"] - second_queen["x"]) == abs(first_queen["y"] - second_queen["y"]):
        return True

    return False


def main():
    # Generate random coords for both queens
    first_queen_coords = {
        "x": random.randint(0, 8),
        "y": random.randint(0, 8),
    }
    second_queen_coords = {
        "x": random.randint(0, 8),
        "y": random.randint(0, 8),
    }

    if can_queens_beat_each_other(first_queen_coords, second_queen_coords):
        print("Yes", first_queen_coords, second_queen_coords)
    else:
        print("No", first_queen_coords, second_queen_coords)


if __name__ == "__main__":
    main()