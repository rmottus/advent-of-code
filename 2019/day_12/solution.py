from __future__ import annotations
from typing import List
from numpy import lcm
import sys

class Moon:
    def __init__(self, init_pos: [int, int, int]):
        self.pos = init_pos
        self.vel = [0, 0, 0]

    def apply_gravity(self, moon: Moon) -> None:
        for i in range(3):
            if self.pos[i] > moon.pos[i]:
                self.vel[i] -= 1
                moon.vel[i] += 1
            elif self.pos[i] < moon.pos[i]:
                self.vel[i] += 1
                moon.vel[i] -= 1

    def advance_time(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def get_total_energy(self) -> int:
        return sum([ abs(i) for i in self.pos ]) * sum([ abs(i) for i in self.vel ])

def simulate_steps(moons: List[Moon], time: int) -> None:
    for time in range(time):
        for i in range(len(moons)):
            first_moon = moons[i]
            for j in range(i+1, len(moons)):
                first_moon.apply_gravity(moons[j])

            first_moon.advance_time()

def main():
    moons = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            pos = [ int(i) for i in [j[2:] for j in line.strip()[1:-1].split(', ')] ]
            moons.append(Moon(pos))

    # Part 1
    # simulate_steps(moons, 1000)
    # print(f"Total energy is {sum(moon.get_total_energy() for moon in moons)}")

    # Part 2
    # We can indivudually calculate periods in each axis, and the answer will be the LCM of the periods of the three axis
    starting_pos = [ [ (moon.pos[axis], moon.vel[axis] ) for moon in moons ] for axis in range(3) ]
    period = {}

    steps = 0
    while len(period) < 3:
        steps += 1
        simulate_steps(moons, 1)

        for axis in range(3):
            if axis not in period and starting_pos[axis] == [ (moon.pos[axis], moon.vel[axis] ) for moon in moons ]:
                period[axis] = steps

    print(f"This universe returns to the starting postion after {lcm.reduce(list(period.values()))}")



if __name__ == '__main__':
    main()