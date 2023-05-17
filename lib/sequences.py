#!/usr/bin/env python3
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
             377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
fibonacci.append(1200)
fibonacci.insert(0, 7)
fibonacci.pop()
fibonacci.remove(7)
del (fibonacci[8:24])
range = range(0, 8)


def print_fibonacci(length):
    pass
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_sequence.append(
                        fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    print(fibonacci_sequence)
