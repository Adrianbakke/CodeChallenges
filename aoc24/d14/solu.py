def solve():
    import sys

    # Dimensions of the area
    width = 101
    height = 103
    time_steps = 100

    # Middle lines
    mid_x = width // 2    # 101//2 = 50
    mid_y = height // 2   # 103//2 = 51

    robots = []
    for line in open("input.txt", "r").read().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        p_part = parts[0][2:] 
        v_part = parts[1][2:]
        
        # Parse positions
        x_str, y_str = p_part.split(',')
        x = int(x_str)
        y = int(y_str)

        # Parse velocity
        dx_str, dy_str = v_part.split(',')
        dx = int(dx_str)
        dy = int(dy_str)

        robots.append((x, y, dx, dy))

    # Simulate 100 seconds
    J = 0
    while True:
        if J%103!=28:
            J+=1
            continue
        new_positions = []
        for (x, y, dx, dy) in robots:
            # Position after 100 seconds:
            # Move x and y with wrap-around
            new_x = (x + dx * J) % width
            new_y = (y + dy * J) % height
            new_positions.append((new_x, new_y))
        
        print(J)
        for r in range(height):
            s = ""
            for c in range(width):
                if (r,c) in new_positions:
                    s += "X"
                else:
                    s += "."     
            print(s)
        J += 1

    # Count how many robots are in each quadrant
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    # for (x, y) in new_positions:
    #     if x == mid_x or y == mid_y:
    #         # On a center line, does not count in any quadrant
    #         continue

    #     if x < mid_x and y < mid_y:
    #         q1 += 1
    #     elif x > mid_x and y < mid_y:
    #         q2 += 1
    #     elif x < mid_x and y > mid_y:
    #         q3 += 1
    #     elif x > mid_x and y > mid_y:
    #         q4 += 1

    # safety_factor = q1 * q2 * q3 * q4
    # print(safety_factor)


if __name__ == "__main__":
    solve()
