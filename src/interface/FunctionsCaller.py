from graphics.rasterization import line_bresenham, line_dda

class FunctionsCaller:
    def caller_line_dda(self, canvas, first_point: tuple, second_point: tuple) -> None:
        line_dda(canvas, first_point, second_point)
    
    def caller_line_bresenham(self, canvas, first_point: tuple, second_point: tuple) -> None:
        line_bresenham(canvas, first_point, second_point)
        