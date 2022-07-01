import math as maths

def main(up_to):
	primes_list = []
	i = 2
	while len(primes_list) < up_to:
		if is_next_prime(i, primes_list):
			primes_list.append(i)
		i += 1
	return(primes_list[-1])

def is_next_prime(n, list):
	for i in list:
		if (maths.floor(pow(n,0.5))+1) < i:
			return(True)
		if n%i==0:
			return(False)
	return(True)

if __name__ == "__main__":
	print(main(10001))