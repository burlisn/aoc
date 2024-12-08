inputData = open("input.txt").read()
grid = []
for line in inputData.splitlines():
    grid.append(list(line))

ans2 = 0

dir = [(-1,0),(0,1),(1,0),(0,-1)]

# find start
gr, gc = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "^":
            gr, gc = r, c

# move
def Walk(gr, gc):
    enc1 = set()
    enc2 = set()
    dirIdx = 0
    while True:
        if (gr, gc, dirIdx) in enc2:
            # Already encountered, in loop
            return len(set()), True
        enc1.add((gr, gc))
        enc2.add((gr, gc, dirIdx))
        
        nr = gr + dir[dirIdx][0]
        nc = gc + dir[dirIdx][1]
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            # Dobby is free, return
            return len(enc1), False
        if grid[nr][nc] != "#":
            gr = nr
            gc = nc
        else:
            dirIdx = (dirIdx + 1) % len(dir)

for r in range(len(grid)):
    for c in range(len(grid[0])):
        # skip guard start and existing crates
        if (grid[r][c] == "^") or (grid[r][c] == "#"):
            continue
        prev = grid[r][c]
        grid[r][c] = "#"
        if Walk(gr, gc)[1]:
            ans2 += 1
        grid[r][c] = prev

print(Walk(gr,gc))
print(ans2)