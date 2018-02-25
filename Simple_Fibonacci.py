# 1 1 2 3 5 8 13 21

# An algorithm is simply a series of steps to solve a problem

import time
import sys

# n = int(input('How many fib values do you want? '))



def fibonacci(n):
    f_num = 1
    sec_num = 1
    counter = 2
    series = [1, 1]
    if n == 2:
        return series
    if n == 1:
        return [1]
    if n == 0:
        return ('Go fuck yourself')
    while counter < n:
        sum = f_num + sec_num
        series.append(sum)
        f_num = sec_num
        sec_num = sum
        counter += 1
    return series

times = 1000
test_value = 1000

print(fibonacci(times))


before_time = time.time()
for _ in range(times):
    fibonacci(test_value)
print(f'This is how long the fibonacci iterative took for {test_value}, {times} times', time.time() - before_time)

# print('Your values are: ',fibonacci())


