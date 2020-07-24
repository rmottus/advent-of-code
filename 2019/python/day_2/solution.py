import sys, copy
from typing import List

def execute_program(noun: int, verb: int, program: List[List[int]]):
    codes = copy.deepcopy(program)
    # set pos 1 and 2 correctly
    codes[0][1] = noun
    codes[0][2] = verb

    for [op, in1, in2, out] in codes:
        if op == 99:
            answer = codes[0][0]
            print(f"Answer for ({noun}, {verb}): {answer}")
            return answer
        elif op == 1:
            codes[out // 4][out % 4] = codes[in1 // 4][in1 % 4] + codes[in2 // 4][in2 % 4]
        elif op == 2:
            codes[out // 4][out % 4] = codes[in1 // 4][in1 % 4] * codes[in2 // 4][in2 % 4]
        else:
            raise Exception(f"Unknown opertion: [{op}, {in1}, {in2}, {out}]")

def main():
    with open(sys.argv[1], 'r') as input:
        all_codes = [ int(i) for i in input.readline().split(",") ]
        codes = [all_codes[i:i+4] for i in range(0, len(all_codes), 4)]

    # First part
    execute_program(12, 2, codes)

    # Second part
    target = 19690720
    noun = 0
    while execute_program(noun + 1, 1, codes) <= target:
        noun += 1

    verb = 0
    while execute_program(noun, verb + 1, codes) <= target:
        verb += 1

    print(f"Formatted answer: {100 * noun + verb}")

if __name__ == '__main__':
    main()