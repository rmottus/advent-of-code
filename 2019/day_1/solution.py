import sys

def calcualte_fuel(mass: int):
    return max(int(mass/3) - 2, 0)

def calcualte_module_fuel(mass: int):
    last_mass = mass
    total_fuel = 0

    while True:
        last_mass = calcualte_fuel(last_mass)
        total_fuel += last_mass
        if last_mass == 0:
            return total_fuel

def main():
    with open(sys.argv[1], 'r') as input:
        fuels = [calcualte_module_fuel(int(line)) for line in input]

    print(f"Total Fuel: {sum(fuels)}")

if __name__ == '__main__':
    main()