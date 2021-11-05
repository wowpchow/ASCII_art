# Created by Justin Wong
# 9/24/21
# convert a string input to a custom ascii printout

# open access to ascii_alphabet.txt
# note the dimenstions of each letter
infile = open("ascii_alphabet.txt",'r')
outfile = open("output.txt",'w')
# enter the string you would like to print
# yes it can handle whitespace too
# will convert all characters to uppercase
print('Enter the string to print: ')
text = input()
text = text.upper()
temp = ""
char_arr = []
num_arr = []

# convert the string input to a character array
# see output for insight (char vs. string)
for idx in text:
	char_arr.append(idx)
print(char_arr)

# convert each character to an ascii integer
# then do math so they represent the line numbers in the ascii_alphabet
# A -> 65 (ASCII)
# 65 - 65 -> 0 * 7 -> 0 ('A' begins at line 0)
# B -> 66 (ASCII)
# 66 - 65 -> 1 * 7 -> 7 ('B' begins at line 7)
for idx in char_arr:
	num_idx = (ord(idx)-65)*7
# adjustment to handle whitespace ' ' with ascii 32
# (32 - 65) * 7 = -231
# add 413 to yield 182 which is the line where I specified the whitespace character to begin
	if num_idx == -231:
		num_idx = num_idx+413
	num_arr.append(num_idx)
print(num_arr)
print("\nPRINTING\n")

# read each line from ascii_alphabet.txt into character array
# print each character line by line (each character is 7 lines)
line = infile.read().splitlines()
for layer in range(7):
	for idx in num_arr:
		# print(line[idx], end=" ")
		temp = temp + " " + line[idx]
	num_arr = [x+1 for x in num_arr]
	outfile.write(temp + "\n")
	# print(temp)
	temp = ""
infile.close()
outfile.close()