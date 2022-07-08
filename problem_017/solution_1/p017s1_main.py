def main(up_to):
	sum = 0
	for i in range(1,up_to+1):
		print(number_to_words(i))
		sum += len(number_to_words(i))
	return(sum)

def number_to_words(number):
	number_string = str(number)
	words_dict = {
		"0" : "",
		"1" : "one",
		"2" : "two",
		"3" : "three",
		"4" : "four",
		"5" : "five",
		"6" : "six",
		"7" : "seven",
		"8" : "eight",
		"9" : "nine",
		"10": "ten",
		"11": "eleven",
		"12": "twelve",
		"13": "thirteen",
		"14": "fourteen",
		"15": "fifteen",
		"16": "sixteen",
		"17": "seventeen",
		"18": "eighteen",
		"19": "nineteen",
		"20": "twenty",
		"30": "thirty",
		"40": "forty",
		"50": "fifty",
		"60": "sixty",
		"70": "seventy",
		"80": "eighty",
		"90": "ninety",
		"1000": "onethousand"}
	if number_string in words_dict:
		return(words_dict[number_string])
	tens = number_string[-2]
	ones = number_string[-1]
	if number < 100:
		return(words_dict[tens+"0"]+words_dict[ones])
	hundereds = number_string[-3]
	if (tens+ones) in words_dict:
		return(words_dict[hundereds]+"hundredand"+words_dict[tens+ones])
	if (tens == "0"):
		if (ones == "0"):
			return(words_dict[hundereds]+"hundred")
		return(words_dict[hundereds]+"hundredand"+words_dict[ones])
	return(words_dict[hundereds]+"hundredand"+words_dict[tens+"0"]+words_dict[ones])


if __name__ == "__main__":
	print(main(1000))