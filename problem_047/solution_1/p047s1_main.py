from common import functions as cf

def main(n):
	i = 1
	while True:
		i += 1
		found = True
		for j in range(n):
			if len(cf.find_prime_factors(i+j,as_dict=True)) < n:
				found = False
				break
		if found:
			return(i)

if __name__ == "__main__":
	print(main(4))
