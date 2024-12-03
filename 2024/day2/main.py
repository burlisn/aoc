import sys
import copy

file = open("input.txt")

ans1 = 0
ans2 = 0

def EvaluateLine(aLine):
  direction = "invalid"
  safe = True
  badHit = False
  for i, value in enumerate(aLine):
    # ignore first value
    if i > 0:
      # set direction
      if direction == "invalid":
        if aLine[i - 1] < value:
          direction = "increasing"
        elif aLine[i - 1] > value:
          direction = "decreasing"
        else:
          safe = False
          break

      # check if safe
      if (direction == "increasing" and aLine[i - 1] > value) or (direction == "decreasing" and aLine[i - 1] < value):
        safe = False
        break
      elif abs(aLine[i - 1] - value) < 1 or abs(aLine[i - 1] - value) > 3:
        safe = False
        break

  return safe

for line in file:
  valuesString = line.split()
  valuesInt = [int(value) for value in valuesString]

  if EvaluateLine(valuesInt):
    ans1 += 1
    ans2 += 1
  else:
    for i, _ in enumerate(valuesInt):
      newLine = copy.deepcopy(valuesInt)
      newLine.pop(i)
      if EvaluateLine(newLine):
        ans2 += 1
        break

print(ans1)
print(ans2)
