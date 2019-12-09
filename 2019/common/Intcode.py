from typing import List
from collections import deque

class Intcode:

    def __init__(self, program: List[int]):
        self._original_program = program.copy()

    def run_program(self, inputs: List[int]):
        self._program = self._original_program.copy()
        input_queue = deque(inputs)
        output_queue = deque()
        instr_ptr = 0
        while True:
            instruction = self._program[instr_ptr]
            op_code = instruction % 100
            pmode_1 = instruction // 100 % 10
            pmode_2 = instruction // 1000 % 10
            pmode_3 = instruction // 10000 % 10

            if op_code == 1:
                first_param = self._get_param(instr_ptr + 1, pmode_1)
                second_param = self._get_param(instr_ptr + 2, pmode_2)

                self._put_param(instr_ptr + 3, first_param + second_param, pmode_3)
                instr_ptr += 4
            elif op_code == 2:
                first_param = self._get_param(instr_ptr + 1, pmode_1)
                second_param = self._get_param(instr_ptr + 2, pmode_2)

                self._put_param(instr_ptr + 3, first_param * second_param, pmode_3)
                instr_ptr += 4
            elif op_code == 3:
                self._put_param(instr_ptr + 1, input_queue.pop(), pmode_1)
                instr_ptr += 2
            elif op_code == 4:
                output_queue.append(self._get_param(instr_ptr + 1, pmode_1))
                instr_ptr += 2
            elif op_code == 5:
                if self._get_param(instr_ptr + 1, pmode_1) != 0:
                    instr_ptr = self._get_param(instr_ptr + 2, pmode_2)
                else:
                    instr_ptr += 3
            elif op_code == 6:
                if self._get_param(instr_ptr + 1, pmode_1) == 0:
                    instr_ptr = self._get_param(instr_ptr + 2, pmode_2)
                else:
                    instr_ptr += 3
            elif op_code == 7:
                first_param = self._get_param(instr_ptr + 1, pmode_1)
                second_param = self._get_param(instr_ptr + 2, pmode_2)

                self._put_param(instr_ptr + 3, 1 if first_param < second_param else 0, pmode_3)
                instr_ptr += 4
            elif op_code == 8:
                first_param = self._get_param(instr_ptr + 1, pmode_1)
                second_param = self._get_param(instr_ptr + 2, pmode_2)

                self._put_param(instr_ptr + 3, 1 if first_param == second_param else 0, pmode_3)
                instr_ptr += 4
            elif op_code == 99:
                return output_queue if len(output_queue) > 0 else self._program[0]
            else:
                raise Exception(f"Unknown op_code: {op_code} at {instr_ptr} of {self._program}")

    def _get_param(self, idx: int, mode: int):
        value = self._program[idx]
        if mode == 0:
            return self._program[value]

        return value

    def _put_param(self, idx: int, output: int, mode: int):
        if mode == 0:
            self._program[self._program[idx]] = output
            return

        self._program[idx] = output