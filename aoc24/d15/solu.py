
input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
input = open("input.txt", "r").read()
B,M=input.split("\n\n")
B=[list(x) for x in B.splitlines()]
R,C=len(B),len(B[0])
M = M.replace("\n","")


def calculate_gps(warehouse):
    gps_sum = 0
    for i, row in enumerate(warehouse):
        for j, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * i + j
    return gps_sum

move_map = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}



def execute_move(robot_pos, direction):
    x, y = robot_pos
    dx, dy = move_map[direction]
    nx, ny = x + dx, y + dy
    moves = [("@",nx,ny)]
    while B[nx][ny] == "O":
        nx+=dx
        ny+=dy
        moves.append(("O",nx,ny))
    if B[nx][ny] == "#":
        return x,y
    for s,r,c in moves:
        B[r][c] = s
    B[x][y] = "."
    return x+dx,y+dy


robot_pos = None
for i, row in enumerate(B):
    for j, cell in enumerate(row):
        if cell == '@':
            robot_pos = (i, j)
            break
    if robot_pos:
        break


for x in B:
    print(x)
print()

for move in M:
    robot_pos = execute_move(robot_pos, move)

gps_sum = calculate_gps(B)
print(gps_sum)

