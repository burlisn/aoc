inputData = open("input.txt").read()

ans1 = 0
ans2 = 0

dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}

grid = inputData.splitlines()

def EvaluateTrail(grid, r, c, reachablePositions):
    if int(grid[r][c]) == 9:
        reachablePositions.add((r, c))
        global ans2
        ans2 += 1
        return
    
    for d in dir:
        if 0 <= r+d[0] < len(grid) and 0 <= c+d[1] < len(grid[0]):
            if int(grid[r][c]) == int(grid[r+d[0]][c+d[1]]) - 1:
                EvaluateTrail(grid, r+d[0], c+d[1], reachablePositions)

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if int(grid[r][c]) == 0:
            reachablePositions = set()
            EvaluateTrail(grid, r, c, reachablePositions)
            ans1 += len(reachablePositions)

print(ans1)
print(ans2)