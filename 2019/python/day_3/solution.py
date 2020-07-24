import sys
from typing import List

def move_in_x(cur_x: int, cur_y: int, distance: int, speed: int, history: List[str]) -> int:
    for i in range(cur_x + speed, cur_x + (distance + 1) * speed, speed):
        history.append(f"{i}:{cur_y}")

    return cur_x + distance * speed

def move_in_y(cur_x: int, cur_y: int, distance: int, speed: int, history: List[str]) -> int:
    for i in range(cur_y + speed, cur_y + (distance + 1) * speed, speed):
        history.append(f"{cur_x}:{i}")

    return cur_y + distance * speed

def create_wire_path(moves: List[str]) -> List[str]: 
    path = []
    x = 0
    y = 0

    for move in moves:
        dir = move[:1]
        distance = int(move[1:])

        if dir == 'R':
            x = move_in_x(x, y, distance, 1, path)
        elif dir == 'L':
            x = move_in_x(x, y, distance, -1, path)
        elif dir == 'U':
            y = move_in_y(x, y, distance, 1, path)
        elif dir == 'D':
            y = move_in_y(x, y, distance, -1, path)
        else:
            raise Exception(f"Something went wrong with move: {move}")

    return path

def get_closest_cross_manhattan(cross_pts: List[str]):
    min = sys.maxsize
    for cross in cross_pts:
        dist = sum([abs(int(z)) for z in cross.split(':')])
        if dist < min:
            min = dist

    print(f"Clostest intersection has distance: {min}")

def get_closest_cross_path_len(cross_pts: List[str], first_path: List[str], second_path: List[str]):
    min = sys.maxsize
    for cross in cross_pts:
        len_first_path = first_path.index(cross) + 1
        len_second_path = second_path.index(cross) + 1
        dist = len_first_path + len_second_path
        if dist < min:
            min = dist

    print(f"Shrotest path to an interestcion has length: {min}")

def main():
    with open(sys.argv[1], 'r') as input:
        first_wire_moves = input.readline().split(",")
        second_wire_moves = input.readline().split(",")

    first_wire = create_wire_path(first_wire_moves)
    second_wire = create_wire_path(second_wire_moves)

    cross_pts = [value for value in first_wire if value in second_wire]
    # Part 1
    get_closest_cross_manhattan(cross_pts)
    # Part 2
    get_closest_cross_path_len(cross_pts, first_wire, second_wire)

if __name__ == '__main__':
    main()