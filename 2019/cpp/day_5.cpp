#include <iostream>
#include <vector>
#include <string>

#include "intcode.h"

int main() {
    std::vector<int> program = std::vector<int>();

    std::string line;
    while (std::getline(std::cin, line, ',')) {
        program.push_back(std::stoi(line));
    }

    IntCode computer(program);
    computer.push_input(5);
    computer.execute();

    while (computer.has_output()) {
        std::cout << "The program output: " << computer.pop_output() << std::endl;
    }
}