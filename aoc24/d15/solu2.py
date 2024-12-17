from copy import deepcopy

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
R,C=len(B),len(B[0])*2
print(R,C)
M = M.replace("\n","")

def scale_map(original_map_lines):
    walls = set()
    boxes = set()
    robot = None
    for r, line in enumerate(original_map_lines):
        col_out = 0
        c = 0
        print(line)
        for c in line:

            if c == '#':
                walls.add((r, col_out))
                walls.add((r, col_out+1))
                col_out += 2
            elif c == '.':
                col_out += 2
            elif c == 'O':
                boxes.add(((r, col_out), (r,col_out+1)))
                col_out += 2
            elif c == '@':
                robot = (r, col_out)
                col_out += 2
    return walls, boxes, robot


def simulate_moves(walls, boxes, robot, moves_str):
    """
    Given sets for walls and boxes, and robot position,
    simulate the moves. Each move is one of '^','v','<','>'.
    Update boxes and robot as moves are applied.
    """
    dirs = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    robot_r, robot_c = robot
    for move in moves_str:
        if move not in dirs:
            continue
        dr, dc = dirs[move]

        nr, nc = robot_r + dr, robot_c + dc

        if (nr, nc) in walls:
            continue  # move blocked

        box = lambda rr,cc: [subset for subset in boxes if (rr,cc) in subset]
        def get_union(rr,cc):
            su = set()
            def _inner(subs):
                for s in subs:
                    if s in su:
                        continue
                    su.add(s)
                    for rr,cc in s:
                        _inner(box(rr,cc))
            _inner(box(rr,cc))
            return su

        if box(nr,nc):
            chain_r, chain_c = nr, nc
            bt = get_union(chain_r, chain_c)
            old_list = deepcopy(bt)
            t = 0
            while len(old_list) > t:
                t = len(old_list)
                for b1,b2 in bt:
                    old_list = get_union(b1[0]+dr, b1[1]+dc) | get_union(b2[0]+dr, b2[1]+dc) | old_list
                bt = deepcopy(old_list)


            push_list = {((b1[0]+dr, b1[1]+dc), (b2[0]+dr, b2[1]+dc)) for b1,b2 in old_list}

            abort = False
            for b in [x for x in push_list]:
                if b[0] in walls or b[1] in walls:
                    abort = True
                    break
            if abort: continue

            for b in [x for x in old_list]:
                boxes.remove(b)
            for b in [x for x in push_list]:
                boxes.add(b)

            robot_r, robot_c = nr, nc

        else:
            robot_r, robot_c = nr, nc

        print_board(walls, boxes, (robot_r, robot_c))

    return boxes, (robot_r, robot_c)


def compute_gps_sum(boxes):
    total = 0

    for b in boxes:
        print("box at", b)
        r,c = b[0]
        total += 100 * r + c
    return total

def print_board(walls, boxes, robot):
    board = [['.' for _ in range(C)] for _ in range(R)]

    for r, c in walls:
        board[r][c] = '#'

    for box in boxes:
        r1,c1 = box[0]
        r2,c2 = box[1]
        board[r1][c1] = '['
        board[r2][c2] = ']'

    rr, rc = robot
    board[rr][rc] = '@'

    for row in board:
        print(''.join(row))


walls, boxes, robot = scale_map(B)
print_board(walls, boxes, robot)

boxes, robot = simulate_moves(walls, boxes, robot, M)
answer = compute_gps_sum(boxes)
print(answer)

