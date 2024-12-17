import copy

inputData = open("input.txt").read()
inputList = list(inputData)
blockList = []

def Swap(aList, nl, nr):
    fs = True # find start or find end?
    needLen = len(aList[nl:nr + 1])
    dl, dr = 0, 0
    for i, item in enumerate(aList):
        if i > nl:
            return
        
        # mark left
        if fs and item == ".":
            dl = i
            fs = False
        if not fs:
            if (i+1 < len(aList) and aList[i+1] != ".") or (i+1 == len(aList)):
                dr = i
                fs = True

                # Check if fit
                if needLen <= len(aList[dl:dr+1]):
                    # print("====")
                    # print(aList)
                    aList[dl:dl+needLen], aList[nl:nr+1] = aList[nl:nr+1], aList[dl:dl+needLen]
                    # print(aList)
                    # print("====")
                    return

        
ans1 = 0
ans2 = 0

empty = False
id = 0
for char in inputList:
    if empty:
        blockList.extend(["."] * int(char))
    else:
        blockList.extend([id] * int(char))
        id += 1
    empty = not empty

blockList2 = copy.deepcopy(blockList)

# furthestLeft = 0
# for i, item in enumerate(reversed(blockList)):
#     if item != ".":
#         startLeft = furthestLeft
#         for leftIndexSlice, itemSlice in enumerate(blockList[startLeft:]):
#             rightIndex = len(blockList) - i - 1
#             furthestLeft = startLeft + leftIndexSlice
#             if itemSlice == "." and startLeft + leftIndexSlice < rightIndex:
#                 blockList[startLeft + leftIndexSlice], blockList[rightIndex] = blockList[rightIndex], blockList[startLeft + leftIndexSlice]
#                 break

listLen = len(blockList2)
fs = True # find start
n = -1
nl, nr = 0, 0
for i, item in enumerate(reversed(blockList2)):
    ti = listLen - i - 1

    # if number == 0, we are done
    if item == 0:
        break

    # encountered new number start, set right
    if fs and item != ".":
        n = item
        nr = ti
        fs = False

    # encountered new number end, set left
    if not fs and blockList2[ti - 1] != n:
        nl = ti
        fs = True

        # perform swap if possible
        Swap(blockList2, nl, nr)


for i, val in enumerate(blockList):
    if val == ".":
        break
    ans1 += val * i

# print(blockList2)
for i, val in enumerate(blockList2):
    if val != ".":
        ans2 += val * i

# print(ans1)
print(ans2)