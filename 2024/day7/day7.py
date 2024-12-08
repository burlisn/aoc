inputData = open("testinput.txt").read()

ans1 = 0
ans2 = 0

# 2314942346457 too low

test = 18446744073709551613
print(test)

def Concatenate(value1, value2):
    return int(str(value1) + str(value2))

def Evaluate(numbers, i, value, result, part2):
    if i == len(numbers) - 1:
        if numbers[i] + value == result or numbers[i] * value == result or (part2 and Concatenate(value, numbers[i]) == result):
            return True
    else: 
        if Evaluate(numbers, i + 1, numbers[i] + value, result, part2) or Evaluate(numbers, i + 1, numbers[i] * value, result, part2) or (part2 and Evaluate(numbers, i + 1, Concatenate(value, numbers[i]), result, part2)):
            return True
    return False

for line in inputData.splitlines():
    result = int(line.split(":")[0])
    nums = [int(value) for value in line.split(":")[1].split()]
    
    if Evaluate(nums, 0, 0, result, False):
        ans1 += result
    if Evaluate(nums, 0, 0, result, True):
        ans2 += result

print(ans1)
print(ans2)