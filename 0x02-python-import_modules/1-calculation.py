#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    answer = add(a, b)
    print(f"{a} + {b} = {answer}")

    answer = sub(a, b)
    print(f"{a} - {b} = {answer}")

    answer = mul(a, b)
    print(f"{a} * {b} = {answer}")

    answer = div(a, b)
    print(f"{a} / {b} = {answer}")
