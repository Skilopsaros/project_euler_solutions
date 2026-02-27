from common import functions as cf

def main(up_to):
	primes = set(cf.find_primes(up_to))
	c_primes = set()
	for prime in primes:
		circular = True
		for rotation in digit_rotations(prime):
			if rotation not in primes:
				circular = False
				break
		if circular:
			c_primes.add(prime)
	return(len(c_primes))

def digit_rotations(n):
	digit_list = list(str(n))
	rotations = []
	for i in range(len(digit_list)-1):
		digit_list.append(digit_list.pop(0))
		rotations.append(int("".join(digit_list)))
	return(rotations)

if __name__ == "__main__":
	print(main(1000000))