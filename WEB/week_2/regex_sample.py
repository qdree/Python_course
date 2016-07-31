import re

file = open('regex_sum_303146.txt')
		
def find_and_sum():
	total = 0
	for line in file:
		line = line.rstrip()
		l_sum = 0
		srch = re.findall('[0-9]+', line)
		for i in srch:
			l_sum = l_sum + int(i)
		total = total + l_sum
	print total


find_and_sum()
file.close()