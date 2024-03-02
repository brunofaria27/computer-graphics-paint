from utils.pixel import set_pixel

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

def line_bresenham(canvas, first_point: tuple, second_point: tuple) -> None:
    dx = abs(second_point[0] - first_point[0])
    dy = abs(second_point[1] - first_point[1])
    x1, y1 = first_point
    x2, y2 = second_point
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        set_pixel(canvas, x1, y1)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    set_pixel(canvas, x2, y2)
