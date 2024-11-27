with open("input.txt", "r") as fin:
    input_lines=fin.read().splitlines()

ans1 = 0
for line in input_lines:
    digits = []
    for i,char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        for j,val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if line[i:].startswith(val):
                digits.append(str(j+1))
    ans1 += int(digits[0]+digits[-1])    
print(ans1)