#include <iostream>
#include <vector>
#include <algorithm>

#include "intcode.h"
#include "utils.h"

int main() {
    std::vector<int> program = load_program_from_cin();

    std::vector<IntCode> amplifiers = {
        IntCode(program),
        IntCode(program),
        IntCode(program),
        IntCode(program),
        IntCode(program)
    };

    int phases[] = {5,6,7,8,9};
    int max_output = 0;

    do {
        // Init all with the phase
        for (int i = 0; i < 5; i++) {
            amplifiers[i].push_input(phases[i]);
        }

        int input = 0;
        do {
            for (int i = 0; i < 5; i++) {
                IntCode &amp = amplifiers[i];
                amp.push_input(input);
                amp.execute();
                
                if (!amp.has_output()) {
                    std::cerr << "No output for amp " << i << std::endl;
                    return -1;
                }
                input = amp.pop_output();
            }
        } while (amplifiers[4].get_state() != IntCodeState::COMPLETE);

        // At this point input is the output of the last amplifier
        if (input > max_output) {
            max_output = input;
        }

        for (auto &amp: amplifiers) {
            amp.reset_memory(program);
        }
    } while (std::next_permutation(phases, phases+5));

    std::cout << "Maximum signal for thrusters is: " << max_output << std::endl;
}