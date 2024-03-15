import math

"""
    Translada os pontos de acordo com os valores de tx e ty.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        tx: O deslocamento em x.
        ty: O deslocamento em y.

    Returns:
        Uma tupla contendo os pontos transladados (start_point, end_point).
"""
def translate(start_point, end_point, tx, ty):
    translated_start_point = (start_point[0] + tx, start_point[1] + ty)
    translated_end_point = (end_point[0] + tx, end_point[1] + ty)
    return translated_start_point, translated_end_point

"""
    Rotaciona os pontos em torno de um centro de acordo com um ângulo.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        angle: O ângulo de rotação em graus.
        center: O centro da rotação no formato (cx, cy).

    Returns:
        Uma tupla contendo os pontos rotacionados (start_point, end_point).
"""
def rotate(start_point, end_point, angle, center):
    cx, cy = center
    radians = math.radians(angle)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
    
    translated_start_x = start_point[0] - cx
    translated_start_y = start_point[1] - cy
    translated_end_x = end_point[0] - cx
    translated_end_y = end_point[1] - cy
    
    rotated_start_x = translated_start_x * cos_theta - translated_start_y * sin_theta
    rotated_start_y = translated_start_x * sin_theta + translated_start_y * cos_theta
    rotated_end_x = translated_end_x * cos_theta - translated_end_y * sin_theta
    rotated_end_y = translated_end_x * sin_theta + translated_end_y * cos_theta
    
    rotated_start_point = (rotated_start_x + cx, rotated_start_y + cy)
    rotated_end_point = (rotated_end_x + cx, rotated_end_y + cy)
    
    return rotated_start_point, rotated_end_point

"""
    Escala os pontos de acordo com um fator de escala em relação a um centro.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        scale_factor: O fator de escala.
        center: O centro da escala no formato (cx, cy).

    Returns:
        Uma tupla contendo os pontos escalados (start_point, end_point).
"""
def scale(start_point, end_point, scale_factor, center):
    cx, cy = center
    scaled_start_x = (start_point[0] - cx) * scale_factor + cx
    scaled_start_y = (start_point[1] - cy) * scale_factor + cy
    scaled_end_x = (end_point[0] - cx) * scale_factor + cx
    scaled_end_y = (end_point[1] - cy) * scale_factor + cy
    
    scaled_start_point = (scaled_start_x, scaled_start_y)
    scaled_end_point = (scaled_end_x, scaled_end_y)
    
    return scaled_start_point, scaled_end_point

"""
    Reflete os pontos em torno de um eixo horizontal.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        center: O centro da reflexão no formato (cx, cy) (opcional).

    Returns:
        Uma tupla contendo os pontos refletidos (start_point, end_point).
"""
def reflect_x(start_point, end_point, center=None):
    if center is None:
        center = (482, 257)
    reflected_start_point = (start_point[0], 2 * center[1] - start_point[1])
    reflected_end_point = (end_point[0], 2 * center[1] - end_point[1])
    return reflected_start_point, reflected_end_point

"""
    Reflete os pontos em torno de um eixo vertical.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        center: O centro da reflexão no formato (cx, cy) (opcional).

    Returns:
        Uma tupla contendo os pontos refletidos (start_point, end_point).
"""
def reflect_y(start_point, end_point, center=None):
    if center is None:
        center = (482, 257)
    reflected_start_point = (2 * center[0] - start_point[0], start_point[1])
    reflected_end_point = (2 * center[0] - end_point[0], end_point[1])
    return reflected_start_point, reflected_end_point

"""
    Reflete os pontos em torno de uma linha diagonal.

    Args:
        start_point: O ponto inicial no formato (x, y).
        end_point: O ponto final no formato (x, y).
        center: O centro da reflexão no formato (cx, cy) (opcional).

    Returns:
        Uma tupla contendo os pontos refletidos (start_point, end_point).
"""
def reflect_xy(start_point, end_point, center=None):
    if center is None:
        center = (482, 257)
    reflected_start_point = (2 * center[0] - start_point[0], 2 * center[1] - start_point[1])
    reflected_end_point = (2 * center[0] - end_point[0], 2 * center[1] - end_point[1])
    return reflected_start_point, reflected_end_point
