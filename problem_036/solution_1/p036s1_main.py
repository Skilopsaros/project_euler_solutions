def main(up_to):
	double_palindromes_sum = 0
	for i in range(1,up_to):
		if is_double_palindrome(i):
			double_palindromes_sum += i
	return(double_palindromes_sum)

def is_double_palindrome(n):
	return((str(n) == str(n)[::-1]) and (str(bin(n))[2:] == str(bin(n))[2:][::-1]))

if __name__ == "__main__":
	print(main(1000000))