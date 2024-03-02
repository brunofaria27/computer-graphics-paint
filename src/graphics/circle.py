from utils.pixel import set_pixel

'''
    Desenha os pontos simétricos de um círculo dado um ponto central e um raio.

    Args:
        canvas: O widget Canvas onde os pontos serão desenhados.
        x: A coordenada x do ponto simétrico.
        y: A coordenada y do ponto simétrico.
        xc: A coordenada x do centro do círculo.
        yc: A coordenada y do centro do círculo.
'''
def plot_circle_points(canvas, x: int, y: int, xc: int, yc: int) -> None:
    set_pixel(canvas, xc + x, yc + y)
    set_pixel(canvas, xc - x, yc + y)
    set_pixel(canvas, xc + x, yc - y)
    set_pixel(canvas, xc - x, yc - y)
    set_pixel(canvas, xc + y, yc + x)
    set_pixel(canvas, xc - y, yc + x)
    set_pixel(canvas, xc + y, yc - x)
    set_pixel(canvas, xc - y, yc - x)

'''
    Algoritmo de Bresenham para desenhar um círculo no canvas.

    Args:
        canvas: O widget Canvas onde o círculo será desenhado.
        point: Uma tupla representando as coordenadas (x, y) do centro do círculo.
        radius: O raio do círculo a ser desenhado.
'''
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
