from utils.pixel import set_pixel

def plot_circle_points(canvas, x: int, y: int, xc: int, yc: int) -> None:
    set_pixel(canvas, xc + x, yc + y)
    set_pixel(canvas, xc - x, yc + y)
    set_pixel(canvas, xc + x, yc - y)
    set_pixel(canvas, xc - x, yc - y)
    set_pixel(canvas, xc + y, yc + x)
    set_pixel(canvas, xc - y, yc + x)
    set_pixel(canvas, xc + y, yc - x)
    set_pixel(canvas, xc - y, yc - x)

def circle_bresenham(canvas, point: tuple, radius: int) -> None:
    x = 0
    y = radius
    p = 3 - 2 * radius
    
    plot_circle_points(canvas, x, y, point[0], point[1])

    while x < y:
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1
        plot_circle_points(canvas, x, y, point[0], point[1])
