#include <vector>
#include <string>
#include <sstream>
#include <stdexcept>
#include <iostream>
#include "intcode.h"

IntCode::IntCode(const std::vector<int> &input)
: length(input.size()), memory(new int[input.size()]), instr(0) {
    // Copy the vector into a fixed sized memory
    std::copy(input.begin(), input.end(), memory);
}

void IntCode::execute() {
    while (true) {
        int op = memory[instr];

        switch(op) {
            case 1:
            {
                int in1_ptr = get_val(instr + 1);
                int in2_ptr = get_val(instr + 2);
                int out_ptr = get_val(instr + 3);
                set_val(out_ptr, get_val(in1_ptr) + get_val(in2_ptr));
                instr += 4;
                break;
            }
            case 2:
            {
                int in1_ptr = get_val(instr + 1);
                int in2_ptr = get_val(instr + 2);
                int out_ptr = get_val(instr + 3);
                set_val(out_ptr, get_val(in1_ptr) * get_val(in2_ptr));
                instr += 4;
                break;
            }
            case 99:
                return;
            default:
                std::ostringstream s = std::ostringstream();
                s << "Unknown opcode: " << op << " at instr " << instr;
                throw std::runtime_error(s.str());
        }
    }
}

void IntCode::print_memory() {
    for (int i = 0; i < length; i++) {
        if (i > 0) {
            std::cout << ",";
        }
        std::cout << memory[i];
    }
    std::cout << std::endl;
}