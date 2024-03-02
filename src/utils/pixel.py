def set_pixel(canvas, x: int, y: int) -> None:
    canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", outline="black")
