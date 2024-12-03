import sys

file = open("input.txt")

ans1 = 0
ans2 = 0
leftList = []
rightList = []

for line in file:
  leftList.append(int(line.split()[0]))
  rightList.append(int(line.split()[1]))

leftList.sort()
rightList.sort()

for i, leftItem in enumerate(leftList):
  ans1 += abs(leftList[i] - rightList[i])

  sameCount = 0
  for rightItem in rightList:
    if leftItem == rightItem:
      sameCount += 1
  ans2 += leftItem * sameCount

print(ans1)
print(ans2)