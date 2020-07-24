#include <iostream>
#include <string>

int get_fuel_for_mass(const int &mass) {
    int fuel = mass / 3 - 2;
    return (fuel < 0 ? 0 : fuel);
}

int get_total_fuel_for_mass(const int &fuel_mass) {
    int fuel = fuel_mass, total_fuel = 0;
    do {
        fuel = get_fuel_for_mass(fuel);
        total_fuel += fuel;
    } while (fuel > 0);

    return total_fuel;
}

int main() {
    int fuel = 0;
    int total_fuel = 0;
    std::string line;
    while (std::getline(std::cin, line)) {
        int mass = std::stoi(line);
        fuel += get_fuel_for_mass(mass);
        total_fuel += get_total_fuel_for_mass(mass);
    }

    std::cout << "Total fuel used for modules excluding fuel: " << fuel << std::endl;
    std::cout << "Total fuel used for modules including fuel: " << total_fuel << std::endl;
}