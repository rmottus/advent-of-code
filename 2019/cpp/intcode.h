#include <vector>
#include <queue>

enum IntCodeState {
    INITIALIZED,
    WAITING_FOR_INPUT,
    RUNNING,
    COMPLETE
};

class IntCode {
    std::vector<int> memory;
    int instr;
    std::queue<int> inputs;
    std::queue<int> outputs;
    IntCodeState state;

    int get_val(const int &i, const int &mode = 0);
    void set_val(const int &i, const int &val, const int &mode = 0);

    public:
        IntCode(const std::vector<int> &input): memory(input), instr(0), state(INITIALIZED) { };
        void execute();
        inline int get_result() { return memory[0]; }
        inline IntCodeState get_state() { return state; }
        inline bool has_output() { return !outputs.empty(); }
        int pop_output();
        inline void push_input(int in) { inputs.push(in); }
        inline void reset_memory(const std::vector<int> &input) {
            memory = input;
            instr = 0;
            state = INITIALIZED;
            std::queue<int>().swap(inputs);
            std::queue<int>().swap(outputs);
        }
        // For debugging
        void print_memory();
};