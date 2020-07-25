#include <vector>
#include <queue>

enum IntCodeState {
    INITIALIZED,
    WAITING_FOR_INPUT,
    COMPLETE
};

class IntCode {
    int *memory;
    const int length;
    int instr;
    std::queue<int> inputs;
    std::queue<int> outputs;

    int get_val(const int &i, const int &mode = 0);
    void set_val(const int &i, const int &val, const int &mode = 0);

    public:
        IntCode(const std::vector<int> &input);
        virtual ~IntCode() { delete memory; };
        IntCodeState execute();
        inline int get_result() { return memory[0]; }
        inline bool has_output() { return !outputs.empty(); }
        int pop_output();
        inline void push_input(const int &in) { inputs.push(in); }
        // For debugging
        void print_memory();
};