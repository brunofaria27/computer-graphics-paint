from graphics.circle import circle_bresenham
from graphics.clipping import clipping_cohen_sutherland, clipping_liang_barsky
from graphics.rasterization import line_bresenham, line_dda

class FunctionsCaller:
    def caller_line_dda(self, canvas, first_point: tuple, second_point: tuple) -> None:
        line_dda(canvas, first_point, second_point)
    
    def caller_line_bresenham(self, canvas, first_point: tuple, second_point: tuple) -> None:
        line_bresenham(canvas, first_point, second_point)
    
    def caller_circle_bresenham(self, canvas, point: tuple, radius: int) -> None:
        circle_bresenham(canvas, point, radius)
    
    def draw_rectangle_overlay(self, canvas, rectangle_coords_first, rectangle_coords_second):
        canvas.create_rectangle(rectangle_coords_first[0], rectangle_coords_first[1],
                                rectangle_coords_second[0], rectangle_coords_second[1],
                                outline="red", width=2, tags="overlay_rectangle")

    def caller_clipping_cohen_sutherland(self, canvas, first_point: tuple, second_point: tuple, rectangle_coords_first: tuple, rectangle_coords_second: tuple) -> None:
        self.draw_rectangle_overlay(canvas, rectangle_coords_first, rectangle_coords_second)

        x_limits = (min(rectangle_coords_first[0], rectangle_coords_second[0]), max(rectangle_coords_first[0], rectangle_coords_second[0]))
        y_limits = (min(rectangle_coords_first[1], rectangle_coords_second[1]), max(rectangle_coords_first[1], rectangle_coords_second[1]))
        is_accepted, clipped_start_point, clipped_end_point = clipping_cohen_sutherland(first_point, second_point, x_limits, y_limits)
        if is_accepted:
            canvas.create_line(clipped_start_point[0], clipped_start_point[1], clipped_end_point[0], clipped_end_point[1], fill="blue", width=2)
            print("Recorte feito com sucesso.")
        else: print("Recorte não pode ser efetuado.")

    def caller_clipping_liang_barsky(self, canvas, first_point: tuple, second_point: tuple, rectangle_coords_first: tuple, rectangle_coords_second: tuple) -> None:
        self.draw_rectangle_overlay(canvas, rectangle_coords_first, rectangle_coords_second)

        x_limits = (min(rectangle_coords_first[0], rectangle_coords_second[0]), max(rectangle_coords_first[0], rectangle_coords_second[0]))
        y_limits = (min(rectangle_coords_first[1], rectangle_coords_second[1]), max(rectangle_coords_first[1], rectangle_coords_second[1]))
        is_accepted, clipped_start_point, clipped_end_point = clipping_liang_barsky(first_point, second_point, x_limits, y_limits)
        if is_accepted:
            canvas.create_line(clipped_start_point[0], clipped_start_point[1], clipped_end_point[0], clipped_end_point[1], fill="blue", width=2)
            print("Recorte feito com sucesso.")
        else: print("Recorte não pode ser efetuado.")