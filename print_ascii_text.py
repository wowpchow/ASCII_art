file = open("ascii_alphabet.txt")

string = 'i love you'
string = string.upper()
char_arr = []
num_arr = []

for idx in string:
    char_arr.append(idx)
print(char_arr)

for idx in char_arr:
    num_idx = (ord(idx)-65)*7
    if num_idx == -231:
        num_idx = num_idx+413
    num_arr.append(num_idx)
print(num_arr)
print("\nPRINTING\n")
line = file.read().splitlines()
for layer in range(7):
    for idx in num_arr:
        print(line[idx], end=" ")
    num_arr = [x+1 for x in num_arr]
    print()