import math as maths
import numpy as np
import timeit

def main(up_to):
	primes_list = []
	for i in range(2, up_to):
		if is_next_prime(i, primes_list):
			primes_list.append(i)
	return(np.sum(np.array(primes_list)))

def is_next_prime(n, list):
	for i in list:
		if (maths.floor(pow(n,0.5))+1) < i:
			return(True)
		if n%i==0:
			return(False)
	return(True)


if __name__ == "__main__":
	print(timeit.timeit("print(main(2000000))","from __main__ import main", number=1))