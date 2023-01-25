#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print(len(sys.argv) - 1, "argument:", end='\n')
        print('1: {}'.format(sys.argv[1]))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(len(sys.argv) - 1, "arguments:", end='\n')
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]), end='\n')
