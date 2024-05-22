#!/usr/bin/env python3

def print_fibonacci(length):
    pass

def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    
    fibonacci_sequence = [0, 1]
    
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    if n == 1:
        fibonacci_sequence = [0]
    
    print(fibonacci_sequence)

print_fibonacci(9)

    