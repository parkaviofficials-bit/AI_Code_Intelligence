import math


class Calculator:

    def add(self, a, b):
        return a + b

    def calculate(self, numbers):
        total = 0

        for number in numbers:
            if number > 0:
                total += number

        return total


def greet(name):
    print("Hello", name)


result = Calculator()
greet("Student")