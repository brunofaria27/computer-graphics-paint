'''
    Determina o código de região de um ponto com base em sua posição relativa ao retângulo fornecido.

    Args:
        x (int): A coordenada x do ponto.
        y (int): A coordenada y do ponto.
        x_limits (tuple): Tupla contendo as coordenadas x mínima e máxima do retângulo.
        y_limits (tuple): Tupla contendo as coordenadas y mínima e máxima do retângulo.

    Returns:
        int: O código de região do ponto.
'''
def region_code(x: int, y: int, x_limits: tuple, y_limits: tuple) -> int:
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    code = 0

    if x < x_min:
        code |= 1
    if x > x_max:
        code |= 2
    if y < y_min:
        code |= 4
    if y > y_max:
        code |= 8
    return code

'''
    Implementa o algoritmo de recorte de linha Cohen-Sutherland para recortar um segmento de linha em relação a uma janela retangular.

    Args:
        canvas: O objeto canvas tkinter onde a linha recortada será desenhada.
        first_point (tuple): Tupla contendo as coordenadas (x, y) do ponto inicial do segmento de linha.
        second_point (tuple): Tupla contendo as coordenadas (x, y) do ponto final do segmento de linha.
        x_limits (tuple): Tupla contendo as coordenadas x mínima e máxima da janela retangular.
        y_limits (tuple): Tupla contendo as coordenadas y mínima e máxima da janela retangular.

    Returns:
        tuple: Uma tupla contendo três elementos:
            - Um booleano indicando se a linha foi aceita (True) ou rejeitada (False).
            - Uma tupla contendo as coordenadas (x, y) do ponto de início recortado.
            - Uma tupla contendo as coordenadas (x, y) do ponto final recortado.
'''
def clipping_cohen_sutherland(canvas, first_point: tuple, second_point: tuple, x_limits: tuple, y_limits: tuple) -> tuple[bool, tuple, tuple]:
    x1, y1 = first_point
    x2, y2 = second_point
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    is_accepted = False

    first_outcode = region_code(x1, y1, x_limits, y_limits)
    second_outcode = region_code(x2, y2, x_limits, y_limits)

    while True:
        if first_outcode == 0 and second_outcode == 0:
            is_accepted = True
            break
        elif first_outcode & second_outcode != 0:
            break
        else:
            outcode = first_outcode if first_outcode != 0 else second_outcode

            if outcode & 1:
                new_x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                new_y = y_max
            elif outcode & 2:
                new_x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                new_y = y_min
            elif outcode & 4:
                new_y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                new_x = x_max
            elif outcode & 8:
                new_y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                new_x = x_min

            if outcode == first_outcode:
                x1, y1 = new_x, new_y
                first_outcode = region_code(x1, y1, x_limits, y_limits)
            else:
                x2, y2 = new_x, new_y
                second_outcode = region_code(x2, y2, x_limits, y_limits)

    clipped_start_point = (x1, y1)               
    clipped_end_point = (x2, y2)
    return is_accepted, clipped_start_point, clipped_end_point 
 
