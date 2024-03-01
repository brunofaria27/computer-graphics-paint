def set_pixel(canvas, x: int, y: int) -> None:
    canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", outline="black")

def line_dda(canvas, first_point: tuple, second_point: tuple) -> None:
    dx = second_point[0] - first_point[0]
    dy = second_point[1] - first_point[1]

    if abs(dx) > abs(dy): steps = abs(dx) 
    else: steps = abs(dy)

    x_incr = dx / steps
    y_incr = dy / steps
    x = first_point[0]
    y = first_point[1]
    set_pixel(canvas, round(x), round(y))

    for _ in range(0, int(steps)):
        x += x_incr
        y += y_incr
        set_pixel(canvas, round(x), round(y))
