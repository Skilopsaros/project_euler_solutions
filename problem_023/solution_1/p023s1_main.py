from common import functions as cf
import copy
import math as maths

def main(upper_limit):
    abundant_numbers_low = find_abundant_numbers(maths.floor(upper_limit/2)+1)
    abundant_numbers_all = find_abundant_numbers(upper_limit)
    sums_of_abundant_numbers = set()
    for i in abundant_numbers_low:
        for j in abundant_numbers_all:
            sums_of_abundant_numbers.add(i+j)
    
    return_sum = 0
    for i in range(upper_limit):
        if i not in sums_of_abundant_numbers:
            return_sum += i
    return(return_sum)


def find_abundant_numbers(up_to, abundant_numbers=[]):
    new_abundant_numbers = copy.copy(abundant_numbers)
    maximum = max(new_abundant_numbers)+1 if new_abundant_numbers else 1
    for i in range(maximum, up_to):
        if cf.sum_of_proper_divisors(i) > i:
            new_abundant_numbers.append(i)
    return(new_abundant_numbers)

if __name__ == "__main__":
    # main(30)
    print(main(28123))