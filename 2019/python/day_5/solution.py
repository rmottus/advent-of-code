import sys
sys.path.append('../')
from common.Intcode import Intcode

def main():
    with open(sys.argv[1], 'r') as program:
        code = [ int(i) for i in program.readline().split(",") ]
    inpt = int(sys.argv[2])

    computer = Intcode(code)
    output = computer.run_program([inpt])
    print(output)

if __name__ == '__main__':
    main()