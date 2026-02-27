import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
	with open(dir_path+"/0042_words.txt") as f:
		words = f.read()
	words_list = words.split('","')
	words_list[0] = words_list[0][1:]
	words_list[-1] = words_list[-1][:-1]

	triangle_numbers = [1]
	add = 2
	while triangle_numbers[-1] < 500:
		triangle_numbers.append(triangle_numbers[-1]+add)
		add+=1
	triangle_numbers = set(triangle_numbers)

	triangle_words = []
	for word in words_list:
		letter_sum = 0
		for letter in word:
			letter_sum += ord(letter) - 64
		if letter_sum in triangle_numbers:
			triangle_words.append(word)

	return(len(triangle_words))
			


if __name__ == "__main__":
	print(main())
