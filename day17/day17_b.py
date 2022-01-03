x_min = 269
x_max = 292
y_min = -68
y_max = -44


def make_one_step(x, y):
    if x > 0:
        x_new = x - 1
    elif x < 0:
        x_new = x + 1
    else:
        x_new = 0
    y_new = y - 1
    return x_new, y_new


def find_max_y_on_trajectory(x, y, x_min, x_max, y_min, y_max):
    x_move, y_move = (x, y)
    x_start, y_start = (x, y)

    flag = True
    while flag:
        if (
            x_min <= x_start
            and x_start <= x_max
            and y_min <= y_start
            and y_start <= y_max
        ):
            return True

        if y_start < y_min or x_start > x_max:
            return False

        x_move, y_move = make_one_step(x_move, y_move)
        x_start = x_start + x_move
        y_start = y_start + y_move


max_y_on_trajectory = []
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        max_y_on_trajectory.append(
            find_max_y_on_trajectory(x, y, x_min, x_max, y_min, y_max)
        )

print(sum(max_y_on_trajectory))
