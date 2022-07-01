
def main():
	palindromes = []
	for i in range(100, 1000):
		for j in range(i, 1000):
			prod = i*j
			if is_palindrome(prod):
				print(i, j, prod)
				palindromes.append(prod)
	return(max(palindromes))


def is_palindrome(input):
	if str(input) == str(input)[::-1]:
		return(True)
	return(False)

if __name__ == "__main__":
	print(main())