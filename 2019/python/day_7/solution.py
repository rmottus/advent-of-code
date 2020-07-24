import sys, itertools
sys.path.append('../')
from common.Intcode import Intcode

def main():
    with open(sys.argv[1], 'r') as program:
        code = [ int(i) for i in program.readline().split(",") ]

    amps = [ Intcode(code) for i in range(5) ]

    max_output = 0
    max_seq = []

    for perm in itertools.permutations([5,6,7,8,9]):
        inpt = 0


        # First time through, pass the phase and the input
        for i in range(5):
            output = amps[i].run_program([perm[i], inpt]).pop()
            inpt = output

        # Keep feedback loop going until last amp has halted
        while not amps[4].halted:
            for i in range(5):
                output = amps[i].run_program([inpt]).pop()
                inpt = output


        for amp in amps:
            amp.reset()
            
        if output > max_output:
            max_output = output
            max_seq = perm

    print(f"Highest signal is {max_output} from sequence {max_seq}")


if __name__ == '__main__':
    main()