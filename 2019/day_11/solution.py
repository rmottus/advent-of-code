import sys, itertools
from typing import List, Dict
sys.path.append('../')
from common.Intcode import Intcode

def paint_hull(code: List[int], starting_colour: int) -> Dict:
    computer = Intcode(code)
    dirs = [ (0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    x = y = 0
    hull = { (x, y): starting_colour }

    while not computer.halted:
        output = computer.run_program([hull.get( (x, y), 0)])

        # Paint the hull
        hull[(x, y)] = output.popleft()
        # Update move the robot
        cur_dir = (cur_dir + 1) if output.popleft() == 1 else (cur_dir - 1)
        cur_dir = cur_dir % len(dirs)
        x += dirs[cur_dir][0]
        y += dirs[cur_dir][1]

    return hull

def print_hull(hull: Dict) -> None:
    min_x = min(hull, key=lambda spot: spot[0])[0]
    max_x = max(hull, key=lambda spot: spot[0])[0]
    min_y = min(hull, key=lambda spot: spot[1])[1]
    max_y = max(hull, key=lambda spot: spot[1])[1]

    
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            print(" " if hull.get((i,j), 0) == 0 else "#", end='')
        print()

def main():
    with open(sys.argv[1], 'r') as program:
        code = [ int(i) for i in program.readline().split(",") ]

    # Part 1
    print(f"Painted {len(paint_hull(code, 0))} spots at least once.")
    # Part 2
    print_hull(paint_hull(code, 1))


if __name__ == '__main__':
    main()