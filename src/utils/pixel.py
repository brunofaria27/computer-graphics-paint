'''
    Desenha um pixel (um pequeno retângulo) no canvas nas coordenadas especificadas.

    Args:
        canvas: O widget Canvas onde o pixel será desenhado.
        x: A coordenada x do pixel.
        y: A coordenada y do pixel.
'''
def set_pixel(canvas, x: int, y: int) -> None:
    canvas.create_rectangle(x, y, x + 1, y + 1, fill="black", outline="black")
