#include <vector>
#include <iostream>
#include <string>

#include "utils.h"

std::vector<int> load_program_from_cin() {
    std::vector<int> program = std::vector<int>();

    std::string line;
    while (std::getline(std::cin, line, ',')) {
        program.push_back(std::stoi(line));
    }

    return program;
}