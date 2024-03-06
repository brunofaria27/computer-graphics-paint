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
def region_code(x: int, y: int, x_min: int, x_max: int, y_min: int, y_max: int) -> int:
    code = 0

    if x < x_min:
        code |= 1
    elif x > x_max:
        code |= 2
    if y < y_min:
        code |= 4
    elif y > y_max:
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
def clipping_cohen_sutherland(first_point: tuple, second_point: tuple, x_limits: tuple, y_limits: tuple) -> tuple[bool, tuple, tuple]:
    x1, y1 = first_point
    x2, y2 = second_point
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    is_accepted = False

    while True:
        first_outcode = region_code(x1, y1, x_min, x_max, y_min, y_max)
        second_outcode = region_code(x2, y2, x_min, x_max, y_min, y_max)

        if first_outcode == 0 and second_outcode == 0:
            is_accepted = True
            break
        elif (first_outcode & second_outcode) != 0: break
        else:
            outcode = first_outcode if first_outcode else second_outcode

            if outcode & 1:
                new_y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                new_x = x_min
            elif outcode & 2:
                new_y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                new_x = x_max
            elif outcode & 4:
                new_x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                new_y = y_min
            elif outcode & 8:
                new_x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                new_y = y_max

            if outcode == first_outcode: x1, y1 = new_x, new_y
            else: x2, y2 = new_x, new_y

    return is_accepted, (x1, y1), (x2, y2)
 
"""
    Função para determinar se uma linha definida pelos coeficientes de sua equação
    paramétrica p*t + q cruza uma região de corte definida por u1 e u2.

    Args:
        p (int): Coeficiente que descreve a mudança de coordenada x.
        q (int): Coeficiente que descreve a mudança de coordenada y.
        u1 (int): Parâmetro que representa o ponto de entrada da interseção.
        u2 (int): Parâmetro que representa o ponto de saída da interseção.

    Returns:
        tuple[bool, int, int]: Uma tupla contendo um valor booleano indicando se
        houve ou não interseção, juntamente com os valores atualizados de u1 e u2.
    """
def clip_test(p: int, q: int, u1: int, u2: int) -> tuple[bool, int, int]:
    result = True
    r = 0

    if p < 0:
        r = q / p
        if r > u2:
            result = False
        elif r > u1:
            u1 = r
    elif p > 0:
        r = q / p
        if r < u1:
            result = False
        elif r < u2:
            u2 = r
    else:
        if q < 0:
            result = False
    return result, u1, u2

"""
    Função que realiza o algoritmo de clipping de Liang-Barsky para recortar uma linha
    definida pelos pontos first_point e second_point em relação aos limites definidos
    por x_limits e y_limits.

    Args:
        first_point (tuple): As coordenadas do primeiro ponto da linha (x1, y1).
        second_point (tuple): As coordenadas do segundo ponto da linha (x2, y2).
        x_limits (tuple): Um par ordenado representando os limites em x (x_min, x_max).
        y_limits (tuple): Um par ordenado representando os limites em y (y_min, y_max).

    Returns:
        tuple[tuple, tuple]: Uma tupla contendo as coordenadas dos pontos resultantes
        após o recorte da linha em relação aos limites.
    """
def clipping_liang_barsky(first_point: tuple, second_point: tuple, x_limits: tuple, y_limits: tuple) -> tuple[tuple, tuple]:
    x1, y1 = first_point
    x2, y2 = second_point
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    u1 = 0
    u2 = 1
    dx = x2 - x1
    dy = y2 - y1

    result_first_if, u1, u2 = clip_test(-dx, x1 - x_min, u1, u2)
    result_second_if, u1, u2 = clip_test(dx, x_max - x1, u1, u2)
    result_third_if, u1, u2 = clip_test(-dy, y1 - y_min, u1, u2)
    result_fourth_if, u1, u2 = clip_test(dy, y_max - y1, u1, u2)
    
    if result_first_if and result_second_if and result_third_if and result_fourth_if:
        if u2 < 1:
            x2 = int(x1 + (u2 * dx))
            y2 = int(y1 + (u2 * dy))
        if u1 > 0:
            x1 = int(x1 + (u1 * dx))
            y1 = int(y1 + (u1 * dy))
    return (x1, y1), (x2, y2)