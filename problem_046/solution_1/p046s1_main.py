from common import functions as cf

def main():
	i = 1
	observes_conjecture = True
	while observes_conjecture:
		i+=1
		composite = 2*i+1
		observes_conjecture = False
		if cf.is_prime(composite):
			observes_conjecture = True
			continue
		primes = cf.find_primes(composite)
		for p in primes:
			if cf.is_perfect_square((composite-p)//2):
				observes_conjecture = True
				break
	return(composite)



if __name__ == "__main__":
	print(main())
