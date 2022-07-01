import math as maths

def main(input):
	check_up_to = input/2
	primes = find_primes(check_up_to)
	print(primes[::-1])
	for prime in primes[::-1]:
		if 0 == (input % prime):
			return(prime)


def find_primes(up_to):
	primes_list = []
	for i in range(maths.ceil(up_to)):
		if is_prime(i):
			primes_list.append(i)
	return(primes_list)

def is_prime(n):
	for i in range(2,maths.floor(pow(n,0.5))+1):
		if n%i==0:
			return(False)
	return(True)


if __name__ == "__main__":
	print(main(1000000))