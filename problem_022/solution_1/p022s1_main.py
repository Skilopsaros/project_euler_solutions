import csv
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def main(file_name):
	with open(dir_path+"/"+file_name) as f:
		names_string = f.readline()
	names_list = names_string.split('","')
	names_list[0] = names_list[0][1:]
	names_list[-1] = names_list[-1][:-1]
	names_list.sort()

	value = 0
	for i, name in enumerate(names_list):
		letter_sum = 0
		for letter in name:
			letter_sum += ord(letter) - 64
		value += (i+1)*letter_sum
	return(value)


if __name__ == "__main__":
	print(main("0022_names.txt"))