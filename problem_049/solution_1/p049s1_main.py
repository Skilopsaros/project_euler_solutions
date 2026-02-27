from common import functions as cf

def main(digits):
	primes = cf.find_primes(pow(10,digits))
	primes_to_remove = []
	for prime in primes:
		if prime < pow(10,digits-1):
			primes_to_remove.append(prime)
	for prime in primes_to_remove:
		primes.remove(prime)
	solutions = []
	for i, p1 in enumerate(primes):
		if p1 == 1487:
			print("1487")
		for j in range(i+1, len(primes)):
			p2 = primes[j]
			p3 = 2*primes[j]-p1
			if p2 == 4817 and p1 == 1487:
				print(p3)
			if cf.is_palindrome(p1,p2) and cf.is_palindrome(p2,p3) and p3 in primes:
				solutions.append([p1,p2,p3])
	return(solutions)



if __name__ == "__main__":
	print(main(4))
