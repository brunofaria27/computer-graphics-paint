import math

"""
    Translada os pontos de acordo com os valores de tx e ty.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        tx: O deslocamento em x.
        ty: O deslocamento em y.

    Returns:
        Uma lista de pontos transladados.
"""
def translate(points, tx, ty):
    translated_points = []
    for x, y in points:
        translated_points.append((x + tx, y + ty))
    return translated_points

"""
    Rotaciona os pontos em torno de um centro de acordo com um ângulo.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        angle: O ângulo de rotação em graus.
        center: O centro da rotação no formato (cx, cy).

    Returns:
        Uma lista de pontos rotacionados.
"""
def rotate(points, angle, center):
    radians = math.radians(angle)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
    cx, cy = center
    rotated_points = []
    for x, y in points:
        translated_x = x - cx
        translated_y = y - cy
        rotated_x = translated_x * cos_theta - translated_y * sin_theta
        rotated_y = translated_x * sin_theta + translated_y * cos_theta
        rotated_points.append((rotated_x + cx, rotated_y + cy))
    return rotated_points

"""
    Escala os pontos de acordo com um fator de escala em relação a um centro.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        scale_factor: O fator de escala.
        center: O centro da escala no formato (cx, cy).

    Returns:
        Uma lista de pontos escalados.
"""
def scale(points, scale_factor, center):
    cx, cy = center
    scaled_points = []
    for x, y in points:
        translated_x = x - cx
        translated_y = y - cy
        scaled_x = translated_x * scale_factor
        scaled_y = translated_y * scale_factor
        scaled_points.append((scaled_x + cx, scaled_y + cy))
    return scaled_points

"""
    Reflete os pontos em torno de um eixo horizontal.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        center: O centro da reflexão no formato (cx, cy).

    Returns:
        Uma lista de pontos refletidos.
"""
def reflect_x(points):
    cx = sum(x for x, _ in points) / len(points)
    reflected_points = [(2 * cx - x, y) for x, y in points]
    return reflected_points

"""
    Reflete os pontos em torno de um eixo vertical.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        center: O centro da reflexão no formato (cx, cy).

    Returns:
        Uma lista de pontos refletidos.
"""
def reflect_y(points):
    cy = sum(y for _, y in points) / len(points)
    reflected_points = [(x, 2 * cy - y) for x, y in points]
    return reflected_points

"""
    Reflete os pontos em torno de uma linha diagonal.

    Args:
        points: Uma lista de pontos no formato [(x1, y1), (x2, y2), ...].
        center: O centro da reflexão no formato (cx, cy).

    Returns:
        Uma lista de pontos refletidos.
"""
def reflect_xy(points):
    cx = sum(x for x, _ in points) / len(points)
    cy = sum(y for _, y in points) / len(points)
    reflected_points = [(2 * cx - x, 2 * cy - y) for x, y in points]
    return reflected_points
