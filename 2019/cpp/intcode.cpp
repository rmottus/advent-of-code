#include <vector>
#include <string>
#include <sstream>
#include <stdexcept>
#include <iostream>
#include "intcode.h"

// ------------- Private ------------- //

int IntCode::get_val(const int &i, const int &mode) {
    const int value = memory[i];
    int ptr;

    switch (mode) {
        case 0:
            ptr = value;
            break;
        case 1:
            return value;
        default:
            throw "Unknown parameter mode";
    }

    return ptr < length ? memory[ptr] : 0;
}

void IntCode::set_val(const int &i, const int &val, const int &mode) {
    int ptr;

    switch (mode) {
        case 0:
            ptr = memory[i];
            break;
        case 1:
            ptr = i;
            break;
        default:
            throw "Unknown parameter mode";
    }

    memory[ptr] = val;
}

// ------------- Public ------------- //

IntCode::IntCode(const std::vector<int> &input)
: length(input.size()), memory(new int[input.size()]), instr(0) {
    // Copy the vector into a fixed sized memory
    std::copy(input.begin(), input.end(), memory);
}

IntCodeState IntCode::execute() {
    while (true) {
        int full_op = memory[instr];
        int op = full_op % 100;
        int in1_mode = (full_op / 100) % 10;
        int in2_mode = (full_op / 1000) % 10;
        int out_mode = (full_op / 10000) % 10;

        switch(op) {
            case 1:
            {
                int in1 = get_val(instr + 1, in1_mode);
                int in2 = get_val(instr + 2, in2_mode);
                set_val(instr + 3, in1 + in2, out_mode);
                instr += 4;
                break;
            }
            case 2:
            {
                int in1 = get_val(instr + 1, in1_mode);
                int in2 = get_val(instr + 2, in2_mode);
                set_val(instr + 3, in1 * in2, out_mode);
                instr += 4;
                break;
            }
            case 3:
                if (inputs.empty()) {
                    // Need to wait for inputs
                    return IntCodeState::WAITING_FOR_INPUT;
                }
                set_val(instr + 1, inputs.front(), out_mode);
                inputs.pop();
                instr += 2;
                break;
            case 4:
            {
                int in1 = get_val(instr + 1, in1_mode);
                outputs.push(in1);
                instr += 2;
                break;
            }
            case 5:
            {
                int in1 = get_val(instr + 1, in1_mode);
                if (in1 != 0) {
                    instr = get_val(instr + 2, in2_mode);
                } else {
                    instr += 3;
                }
                break;
            }
            case 6:
            {
                int in1 = get_val(instr + 1, in1_mode);
                if (in1 == 0) {
                    instr = get_val(instr + 2, in2_mode);
                } else {
                    instr += 3;
                }
                break;
            }
            case 7:
            {
                int in1 = get_val(instr + 1, in1_mode);
                int in2 = get_val(instr + 2, in2_mode);
                set_val(instr + 3, in1 < in2 ? 1 : 0, out_mode);
                instr += 4;
                break;
            }
            case 8:
            {
                int in1 = get_val(instr + 1, in1_mode);
                int in2 = get_val(instr + 2, in2_mode);
                set_val(instr + 3, in1 == in2 ? 1 : 0, out_mode);
                instr += 4;
                break;
            }
            case 99:
                return IntCodeState::COMPLETE;
            default:
                std::ostringstream s = std::ostringstream();
                s << "Unknown opcode: " << op << " at instr " << instr;
                throw std::runtime_error(s.str());
        }
    }
}

int IntCode::pop_output() {
    if (outputs.empty()) {
        throw "There are no outputs";
    }
    const int val = outputs.front();
    outputs.pop();
    return val;
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