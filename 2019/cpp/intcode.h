#include <vector>

class IntCode {
    int *memory;
    const int length;
    int instr;
    bool halted = false;

    inline int get_val(const int &i) { return memory[i]; };
    inline void set_val(const int &i, const int &val) { memory[i] = val; };

    public:
        IntCode(const std::vector<int> &input);
        virtual ~IntCode() { delete memory; };
        void execute();
        inline int get_result() { return get_val(0); }
        // For debugging
        void print_memory();
};