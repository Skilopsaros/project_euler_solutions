import copy

def main():
	# pandigital_pairs = []
	pandigital_prods = set()
	for i in range(98764):
		for j in range(i+1, 98765):
			if len(str(i) + str(j) + str(i*j)) > 10:
				break
			if is_pandigital(i,j):
				# pandigital_pairs.append((i,j))
				pandigital_prods.add(i*j)
	# for pair in pandigital_pairs:
	# 	print(f"pair: {pair}, product {pair[0]*pair[1]}")
	return(sum(pandigital_prods))

def is_pandigital(a,b):
	digits = str(a) + str(b) + str(a*b)
	return(len(digits) == 9 and all([str(d) in digits for d in range(1,10)]))

if __name__ == "__main__":
	print(main())