# This is a python calculator code
message = "This is a calculator that would enable to to calculate simple " \
          "computation in addition, subtraction, multiplication and division"
print(message)

print("Type add for addition, sub for subtraction, div for division and multiply for multiplication")
first_input = input()

print("input the two number you would have to compute")
second_input = int(input())
seconde_input = int(input())

def add(a, b):
    addy = a + b
    return addy


def subtraction(a, b):
    sub = a - b
    return sub


def division(a, b):
    yh = a / b
    return yh


def multiply(a, b):
    mult = a * b
    return mult


if first_input == str("add"):
    print(add(second_input, seconde_input))

elif first_input == str("sub"):
    print(subtraction(second_input, seconde_input))
elif first_input == str("div"):
    print(division(second_input, seconde_input))
elif first_input == str("multiply"):
    print(multiply(second_input, seconde_input))
