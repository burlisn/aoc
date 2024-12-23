ans1 = 0
ans2 = 0

inputData = open("input.txt").read()
stones = [int(stone) for stone in inputData.split()]

encounteredStones = dict()

def EvaluateStone(stone, blink):
    stoneValue = 0

    if blink == 0:
        return 1
    
    if (stone, blink) in encounteredStones:
        return encounteredStones[(stone, blink)]

    stoneStr = str(stone)
    if stone == 0:
        stoneValue = EvaluateStone(1, blink - 1)
    elif len(stoneStr) % 2 == 0:
        mid = len(stoneStr) // 2
        stoneValue = EvaluateStone(int(stoneStr[:mid]), blink - 1) + EvaluateStone(int(stoneStr[mid:]), blink - 1)
    else:
        stoneValue = EvaluateStone(stone * 2024, blink - 1)
    
    encounteredStones[(stone, blink)] = stoneValue
    return stoneValue
    
for stone in stones:
    ans1 += EvaluateStone(stone, 25)
    ans2 += EvaluateStone(stone, 75)

print(ans1)
print(ans2)