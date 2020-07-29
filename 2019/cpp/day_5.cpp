#include <iostream>
#include <vector>

#include "intcode.h"
#include "utils.h"

int main() {
    std::vector<int> program = load_program_from_cin();

    IntCode computer(program);
    computer.push_input(5);
    computer.execute();

    while (computer.has_output()) {
        std::cout << "The program output: " << computer.pop_output() << std::endl;
    }
}