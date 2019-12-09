from typing import List
from collections import deque

class Intcode:

    def __init__(self, program: List[int]):
        self._original_program = program.copy()
        self._program = self._original_program.copy()
        self._instr_ptr = 0
        self.halted = False

    def run_program(self, inputs: List[int]):
        input_queue = deque(inputs)
        output_queue = deque()
        while True:
            instruction = self._program[self._instr_ptr]
            op_code = instruction % 100
            pmode_1 = instruction // 100 % 10
            pmode_2 = instruction // 1000 % 10
            pmode_3 = instruction // 10000 % 10

            if op_code == 1:
                first_param = self._get_param(self._instr_ptr + 1, pmode_1)
                second_param = self._get_param(self._instr_ptr + 2, pmode_2)

                self._put_param(self._instr_ptr + 3, first_param + second_param, pmode_3)
                self._instr_ptr += 4
            elif op_code == 2:
                first_param = self._get_param(self._instr_ptr + 1, pmode_1)
                second_param = self._get_param(self._instr_ptr + 2, pmode_2)

                self._put_param(self._instr_ptr + 3, first_param * second_param, pmode_3)
                self._instr_ptr += 4
            elif op_code == 3:
                if len(input_queue) == 0:
                    # We are out of inputs, return for now and wait to be called again
                    return output_queue
                self._put_param(self._instr_ptr + 1, input_queue.popleft(), pmode_1)
                self._instr_ptr += 2
            elif op_code == 4:
                output_queue.append(self._get_param(self._instr_ptr + 1, pmode_1))
                self._instr_ptr += 2
            elif op_code == 5:
                if self._get_param(self._instr_ptr + 1, pmode_1) != 0:
                    self._instr_ptr = self._get_param(self._instr_ptr + 2, pmode_2)
                else:
                    self._instr_ptr += 3
            elif op_code == 6:
                if self._get_param(self._instr_ptr + 1, pmode_1) == 0:
                    self._instr_ptr = self._get_param(self._instr_ptr + 2, pmode_2)
                else:
                    self._instr_ptr += 3
            elif op_code == 7:
                first_param = self._get_param(self._instr_ptr + 1, pmode_1)
                second_param = self._get_param(self._instr_ptr + 2, pmode_2)

                self._put_param(self._instr_ptr + 3, 1 if first_param < second_param else 0, pmode_3)
                self._instr_ptr += 4
            elif op_code == 8:
                first_param = self._get_param(self._instr_ptr + 1, pmode_1)
                second_param = self._get_param(self._instr_ptr + 2, pmode_2)

                self._put_param(self._instr_ptr + 3, 1 if first_param == second_param else 0, pmode_3)
                self._instr_ptr += 4
            elif op_code == 99:
                self.halted = True
                return output_queue if len(output_queue) > 0 else self._program[0]
            else:
                raise Exception(f"Unknown op_code: {op_code} at {self._instr_ptr} of {self._program}")

    def reset(self):
        self._program = self._original_program.copy()
        self._instr_ptr = 0
        self.halted = False

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