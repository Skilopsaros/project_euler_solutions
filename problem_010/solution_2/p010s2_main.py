import math as maths
import numpy as np
import timeit

def main(up_to):
	primes =[2]
	prime_multiples = [2]
	number = 3
	while number <= up_to:
		for i, p in enumerate(primes):
			while prime_multiples[i] < number:
				prime_multiples[i] += p
		if not (number in prime_multiples):
			print(number)
			primes.append(number)
			prime_multiples.append(number)
		number += 1

	return(primes)


if __name__ == "__main__":
	print(main(2000000))
	#print(timeit.timeit("print(main())"))