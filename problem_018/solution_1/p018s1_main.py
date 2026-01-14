import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def main(file_name):
	lines = file_to_lists(file_name)
	r_lines = lines[::-1]
	for l, line in enumerate(r_lines[1:]):
		for n, _ in enumerate(line):
			r_lines = sum_with_larger_child(r_lines, l+1, n)
	return(r_lines[-1][0])

def sum_with_larger_child(lines, l, n):
	add_child = lines[l-1][n]
	child_2 = lines[l-1][n+1]
	if add_child < child_2:
		add_child = child_2
	lines[l][n] = lines[l][n] + add_child
	return(lines)

def file_to_lists(file_name):
	with open(dir_path+"/"+file_name) as file_in:
		lines = []
		for line in file_in:
			str_list = line.split(" ")
			if str_list[-1][-1] == "\n":
				str_list[-1] = str_list[-1][:-1]
			int_list = []
			for num_str in str_list:
				int_list.append(int(num_str))
			lines.append(int_list)
	return(lines)


if __name__ == "__main__":
	print(main("p018_triangle.txt"))