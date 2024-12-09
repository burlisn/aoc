inputData = open("input.txt").read()

grid = inputData.splitlines()

Rows = len(grid)
Columns = len(grid[0])
antinodes = set()
antinodes2 = set()

tempGrid = []
for r in range(Rows):
    tempGrid.append([])
    for c in range(Columns):
        tempGrid[r].append(".")

def PrintGrid(grid):
    string = ""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            string += grid[r][c]
        string += "\n"
    print(string)

def MarkAntinode(oR, oC):
    global antinodes
    global antinodes2
    for r in range(Rows):
        for c in range(Columns):
            if r == oR and c == oC:
                antinodes2.add((r, c))
                continue
            elif grid[r][c] == grid[oR][oC]:
                dR = r - oR
                dC = c - oC
                if 0 <= oR - dR < Rows and 0 <= oC - dC < Columns:
                    antinodes.add((oR - dR, oC - dC))
                if 0 <= r + dR < Rows and 0 <= c + dC < Columns:
                    antinodes.add((r + dR, c + dC))
                i = 1
                while 0 <= oR - dR * i < Rows and 0 <= oC - dC * i < Columns:
                    antinodes2.add((oR - dR * i, oC - dC * i))
                    i += 1
                i = 1
                while 0 <= r + dR * i < Rows and 0 <= c + dC * i < Columns:
                    antinodes2.add((r + dR * i, c + dC * i))
                    i += 1
            
for r in range(Rows):
    for c in range(Columns):
        if (grid[r][c] != "."):
            MarkAntinode(r, c)

print(len(antinodes))
print(len(antinodes2))