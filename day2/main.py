with open("test_input.txt", "r") as fin:
    input_lines=fin.read().splitlines()

cube_limit = {"red": 12, "green": 13, "blue": 14}
ans1 = 0
ans2 = 0

for line in input_lines:
    valid = True
    game_num, game_info = line.split(":")
    game_num = int(game_num.split()[1])
    events = game_info.split(";")
    cube_maxes = {"red": 0, "green": 0, "blue":0 }
    for event in events:
        cubes = event.split(",")
        for cube in cubes:
            number, color = cube.split()
            if cube_limit[color] < int(number):
                valid = False
            if cube_maxes[color] < int(number):
                cube_maxes[color] = int(number)
    if valid:
        ans1 += game_num
    ans2 += cube_maxes.get("red") * cube_maxes.get("green") * cube_maxes.get("blue")

print(ans1)
print(ans2)