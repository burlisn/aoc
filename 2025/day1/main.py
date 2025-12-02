input = open("input.txt", "r")

numberOfEndZeros = 0
numberOfZerosReached = 0

dail = 50

for line in input:
  DIRECTION = line[0]
  DISTANCE = int(line[1:])

  # Find distance to zero
  distanceToZero = 0
  if dail == 0:
    distanceToZero = 100
  elif DIRECTION == "R":
    distanceToZero = 100 - dail
  elif DIRECTION == "L":
    distanceToZero = dail

  # Find the new dail position
  if DIRECTION == "R":
    dail = (dail + DISTANCE) % 100
  elif DIRECTION == "L":
    dail = (dail - DISTANCE) % 100

  # Calculate number of zeros reached
  remainingDistance = DISTANCE
  remainingDistance = remainingDistance - distanceToZero
  if remainingDistance >= 0:
    # First zero reached
    numberOfZerosReached += 1
    # Additional zeros reached via full loop
    numberOfZerosReached += int(remainingDistance / 100)

  if dail == 0:
    numberOfEndZeros += 1

print(numberOfEndZeros)
print(numberOfZerosReached)