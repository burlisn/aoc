import re

inputData = open("input.txt").read()

ans1 = 0
ans2 = 0

onOffList = [[0, True]]
for on in re.finditer(r"do\(\)", inputData):
    onOffList.append([on.start(), True])
for off in re.finditer(r"don't\(\)", inputData):
    onOffList.append([off.start(), False])
onOffList = sorted(onOffList, key=lambda x: x[0])
print(onOffList)

def IsOn(val):
    prevVal = None
    for onOff in onOffList:
        if val < onOff[0]:
            return prevVal[1]
        prevVal = onOff
    return prevVal[1]

for mul in re.finditer(r"mul\([0-9]+,[0-9]+\)", inputData):
    values = re.findall(r"[0-9]+", mul.group())
    ans1 += int(values[0]) * int(values[1])
    if IsOn(mul.start()):
        ans2 += int(values[0]) * int(values[1])

print(ans1)
print(ans2)