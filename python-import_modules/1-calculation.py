#!/usr/bin/python3
if __name__ == "__main__":
    import calculator
    print('{0} + {1} ='.format(10, 5),calculator.add(10, 5))
    print('{0} - {1} ='.format(10, 5),calculator.sub(10, 5 ))
    print('{0} * {1} ='.format(10, 5),calculator.mul(10, 5 ))
    print('{0} / {1} ='.format(10, 5),calculator.div(10, 5 ))
