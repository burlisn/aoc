import copy
import functools

inputData = open("input.txt").read()
ruleData = inputData.split("\n\n")[0]
listData = inputData.split("\n\n")[1]

ans1 = 0
ans2 = 0

# dictionary entries hold numbers that must come after
rules = {}
for line in ruleData.splitlines():
    nums = [int(x) for x in line.split("|")]
    if nums[0] not in rules:
        rules[nums[0]] = [nums[1]]
    else:
        rules[nums[0]].append(nums[1])

print(rules)

# val2 is further in the list than val1. Make sure this follows the rules.
def Compare(val1, val2):
    if val2 in rules:
        for rule in rules[val2]:
            if rule == val1:
                return -1
        return 1
    return 0
        
for line in listData.splitlines():
    valid = True
    list = [int(x) for x in line.split(",")]
    sortedList = copy.deepcopy(list)
    sortedList.sort(key=functools.cmp_to_key(Compare), reverse=True)
    for i, item in enumerate(list):
        for subItem in list[:i]:
            if Compare(subItem, item) == -1:
                valid = False
                break

    # check if valid
    if valid:
        ans1 += list[(len(list) - 1)//2]
    else:
        ans2 += sortedList[(len(sortedList) - 1)//2]

print(ans1)
print(ans2)
