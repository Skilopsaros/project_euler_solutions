import math as maths
from common import functions as cf

def main(up_to):
	primes_list = []
	i = 2
	while len(primes_list) < up_to:
		if cf.is_next_prime(i, primes_list):
			primes_list.append(i)
		i += 1
	return(primes_list[-1])

if __name__ == "__main__":
	print(main(10001))