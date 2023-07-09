#!/usr/bin/env python3

def print_fibonacci(length):
    fibo = []
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        for i in range(length):
            if(i == 0 or i == 1):
                fibo.append(i)
            else:
                fibo.append(fibo[i - 1] + fibo[i - 2])
        print(fibo)