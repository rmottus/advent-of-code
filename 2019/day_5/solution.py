import sys, copy
from typing import List

def get_param(idx: int, mode: int, program: List[int]):
    value = program[idx]
    if mode == 0:
        return program[value]

    return value

def put_param(idx: int, output: int, mode: int, program: List[int]):
    if mode == 0:
        program[program[idx]] = output
        return

    program[idx] = output

def execute_program(program: List[int], inpt: int):
    code = copy.deepcopy(program)
    instr_ptr = 0
    
    while True:
        instruction = program[instr_ptr]
        op_code = instruction % 100
        pmode_1 = instruction // 100 % 10
        pmode_2 = instruction // 1000 % 10
        pmode_3 = instruction // 10000 % 10

        if op_code == 1:
            first_param = get_param(instr_ptr + 1, pmode_1, program)
            second_param = get_param(instr_ptr + 2, pmode_2, program)

            put_param(instr_ptr + 3, first_param + second_param, pmode_3, program)
            instr_ptr += 4
        elif op_code == 2:
            first_param = get_param(instr_ptr + 1, pmode_1, program)
            second_param = get_param(instr_ptr + 2, pmode_2, program)

            put_param(instr_ptr + 3, first_param * second_param, pmode_3, program)
            instr_ptr += 4
        elif op_code == 3:
            put_param(instr_ptr + 1, inpt, pmode_1, program)
            instr_ptr += 2
        elif op_code == 4:
            print(get_param(instr_ptr + 1, pmode_1, program))
            instr_ptr += 2
        elif op_code == 5:
            if get_param(instr_ptr + 1, pmode_1, program) != 0:
                instr_ptr = get_param(instr_ptr + 2, pmode_2, program)
            else:
                instr_ptr += 3
        elif op_code == 6:
            if get_param(instr_ptr + 1, pmode_1, program) == 0:
                instr_ptr = get_param(instr_ptr + 2, pmode_2, program)
            else:
                instr_ptr += 3
        elif op_code == 7:
            first_param = get_param(instr_ptr + 1, pmode_1, program)
            second_param = get_param(instr_ptr + 2, pmode_2, program)

            put_param(instr_ptr + 3, 1 if first_param < second_param else 0, pmode_3, program)
            instr_ptr += 4
        elif op_code == 8:
            first_param = get_param(instr_ptr + 1, pmode_1, program)
            second_param = get_param(instr_ptr + 2, pmode_2, program)

            put_param(instr_ptr + 3, 1 if first_param == second_param else 0, pmode_3, program)
            instr_ptr += 4
        elif op_code == 99:
            break
        else:
            raise Exception(f"Unknown op_code: {op_code} at {instr_ptr} of {program}")

def main():
    with open(sys.argv[1], 'r') as program:
        code = [ int(i) for i in program.readline().split(",") ]
    inpt = int(sys.argv[2])

    # First part
    execute_program(code, inpt)

if __name__ == '__main__':
    main()