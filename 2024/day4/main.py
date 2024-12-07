inputData = open("input.txt").read()

ans1 = 0
ans2 = 0

grid = inputData.splitlines()
dir = [(1, 0), (1, 1), (0, 1), (-1 , 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
dir2 = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

print(ord("S"))

for r in range(len(grid)):
    for c in range(len(grid[0])):
        for dx, dy in dir:
            if ((r + 3 * dx) not in range(len(grid))) or ((c + 3 * dy) not in range(len(grid[0]))):
                continue
            word = ""
            for i in range(4):
                word += grid[r + i * dx][c + i * dy]
            if word == "XMAS":
                ans1 += 1

        if grid[r][c] == "A":
            valid = True
            if not (r + 1 in range(len(grid)) and r - 1 in range(len(grid)) and c + 1 in range(len(grid[0])) and c - 1 in range(len(grid[0]))):
                continue
            if ord(grid[r + 1][c + 1]) + ord(grid[r - 1][c - 1]) != ord("M") + ord("S") or ord(grid[r + 1][c - 1]) + ord(grid[r - 1][c + 1]) != ord("M") + ord("S"):
                valid = False
            if valid:
                ans2 += 1
            

print(ans1)
print(ans2)