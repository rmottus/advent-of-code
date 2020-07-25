#include <iostream>
#include <string>
#include <vector>

#include "intcode.h"

int run_with_inputs(std::vector<int> &program, const int noun, const int verb) {
    program[1] = noun;
    program[2] = verb;

    IntCode computer = IntCode(program);
    computer.execute();
    return computer.get_result();
}

int main() {
    std::vector<int> program = std::vector<int>();

    std::string line;
    while (std::getline(std::cin, line, ',')) {
        program.push_back(std::stoi(line));
    }

    int result = run_with_inputs(program, 12, 2);
    std::cout << "The result of program for part (12, 2) is: " << result << std::endl;

    // Second part
    int target = 19690720;
    int noun = 1;
    int verb = 1;
    while ((result = run_with_inputs(program, noun + 1, 1)) <= target) {
        noun += 1;
    }
    while (run_with_inputs(program, noun, verb + 1) <= target) {
        verb += 1;
    }

    std::cout << "The inputs (" << noun << ", " << verb << ") results in " << target << std::endl;
}