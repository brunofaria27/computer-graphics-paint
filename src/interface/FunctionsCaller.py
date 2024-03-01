from graphics.rasterization import line_dda

class FunctionsCaller:
    def caller_line_dda(self, canvas, first_point: tuple, second_point: tuple) -> None:
        line_dda(canvas, first_point, second_point)
        