#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    sum = 0
    n = len(sys.argv)
    if n == 1:
        print('0')
    else:
        for i in range(1, n):
            sum += int(sys.argv[i])
        print(sum)
