import tkinter as tk
from graphics.transformations import reflect_x, reflect_xy, reflect_y, rotate, scale, translate

from interface.FunctionsCaller import FunctionsCaller

class Application:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Definir o tamanho inicial da janela e canvas e centralizá-la na tela
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        initial_width = int(screen_width * 0.7)
        initial_height = int(screen_height * 0.85)
        canvas_width = int(screen_width * 0.5)
        canvas_height = int(screen_height * 0.5)
        x = (screen_width - initial_width) // 2
        y = (screen_height - initial_height) // 2
        self.window.geometry(f"{initial_width}x{initial_height}+{x}+{y}")

        # Slide input radius
        self.radius_frame = tk.Frame(self.window)
        self.radius_frame.pack()

        self.radius_label = tk.Label(self.radius_frame, text="Raio para circunferência Bresenham (1-100):")
        self.radius_label.grid(row=0, column=0)
        self.radius_scale = tk.Scale(self.radius_frame, from_=1, to=100, orient=tk.HORIZONTAL)
        self.radius_scale.grid(row=0, column=1)

        # Slide dx, dy -> translate
        self.dx_translate = tk.Frame(self.window)
        self.dx_translate.pack()
        self.dy_translate = tk.Frame(self.window)
        self.dy_translate.pack()

        self.dx_label = tk.Label(self.dx_translate, text="DX:")
        self.dx_label.grid(row=1, column=0)
        self.dx_scale = tk.Scale(self.dx_translate, from_=(-200), to=200, orient=tk.HORIZONTAL)
        self.dx_scale.grid(row=1, column=1)

        self.dy_label = tk.Label(self.dy_translate, text="DY:")
        self.dy_label.grid(row=1, column=0)
        self.dy_scale = tk.Scale(self.dy_translate, from_=(-200), to=200, orient=tk.HORIZONTAL)
        self.dy_scale.grid(row=1, column=1)

        # Slide para pegar angulo
        self.angle_transformation = tk.Frame(self.window)
        self.angle_transformation.pack()

        self.angle_transformation_label = tk.Label(self.angle_transformation, text="Ângulo:")
        self.angle_transformation_label.grid(row=2, column=0)
        self.angle_transformation_scale = tk.Scale(self.angle_transformation, from_=0, to=360, orient=tk.HORIZONTAL)
        self.angle_transformation_scale.grid(row=2, column=1)

        # Entrada fator de escala
        self.scale_factor = tk.Frame(self.window)
        self.scale_factor.pack()

        self.scale_factor_label = tk.Label(self.scale_factor, text="Fator da escala:")
        self.scale_factor_label.grid(row=4, column=0)
        self.scale_factor_entry = tk.Entry(self.scale_factor)
        self.scale_factor_entry.grid(row=4, column=1)

        # Criar o canvas com borda
        self.canvas = tk.Canvas(self.window, bg="white", width=canvas_width, height=canvas_height, bd=2, relief="ridge")
        self.canvas.pack()

        # Texto para mostrar os pontos selecionados
        self.first_point_text = tk.StringVar()
        self.first_point_label = tk.Label(self.window, textvariable=self.first_point_text)
        self.first_point_label.pack()

        self.second_point_text = tk.StringVar()
        self.second_point_label = tk.Label(self.window, textvariable=self.second_point_text)
        self.second_point_label.pack()

        self.rectangle_first_point_text = tk.StringVar()
        self.rectangle_first_point_label = tk.Label(self.window, textvariable=self.rectangle_first_point_text)
        self.rectangle_first_point_label.pack()

        self.rectangle_second_point_text = tk.StringVar()
        self.rectangle_second_point_label = tk.Label(self.window, textvariable=self.rectangle_second_point_text)
        self.rectangle_second_point_label.pack()

        self.center_point_text = tk.StringVar()
        self.center_point_label = tk.Label(self.window, textvariable=self.center_point_text)
        self.center_point_label.pack()

        # Inicializar variáveis importantes
        self.value_first_point = tuple()
        self.value_second_point = tuple()
        self.value_rectangle_first = tuple()
        self.value_rectangle_second = tuple()
        self.value_center_point = tuple()
        self.point_count = 0
        self.rectangle_point_count = 0

        # Inicializar objetos importantes
        functions_caller = FunctionsCaller()

        # Opções do menu
        self.menu = tk.Menu(window)
        window.config(menu=self.menu)

        self.rasterization_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Rasterização", menu=self.rasterization_menu)
        self.rasterization_menu.add_command(label="DDA", command=lambda: functions_caller.caller_line_dda(self.canvas, self.value_first_point, self.value_second_point))
        self.rasterization_menu.add_command(label="Bresenham retas", command=lambda: functions_caller.caller_line_bresenham(self.canvas, self.value_first_point, self.value_second_point))
        self.rasterization_menu.add_command(label="Bresenham circunferência", command=lambda: functions_caller.caller_circle_bresenham(self.canvas, self.value_first_point, int(self.radius_scale.get())))

        self.transformation_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Transformações geométricas", menu=self.transformation_menu)
        self.transformation_menu.add_command(label="Translação", command=lambda: self.transform_and_drawn(lambda points: translate(points, int(self.dx_scale.get()), int(self.dy_scale.get()))))
        self.transformation_menu.add_command(label="Rotação", command=lambda: self.transform_and_drawn(lambda points: rotate(points, int(self.angle_transformation_scale.get()), self.value_center_point)))
        self.transformation_menu.add_command(label="Escala", command=lambda: self.transform_and_drawn(lambda points: scale(points, float(self.scale_factor_entry.get()), self.value_center_point)))
        self.transformation_menu.add_command(label="Reflexão X", command=lambda: self.transform_and_drawn(lambda points: reflect_x(points, self.value_center_point)))
        self.transformation_menu.add_command(label="Reflexão Y", command=lambda: self.transform_and_drawn(lambda points: reflect_y(points, self.value_center_point)))
        self.transformation_menu.add_command(label="Reflexão XY", command=lambda: self.transform_and_drawn(lambda points: reflect_xy(points, self.value_center_point)))

        self.clipping_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Clipping", menu=self.clipping_menu)
        self.clipping_menu.add_command(label="Cohen-Sutherland", command=lambda: functions_caller.caller_clipping_cohen_sutherland(self.canvas, self.value_first_point, self.value_second_point, self.value_rectangle_first, self.value_rectangle_second))
        self.clipping_menu.add_command(label="Liang-Barsky", command=lambda: functions_caller.caller_clipping_liang_barsky(self.canvas, self.value_first_point, self.value_second_point, self.value_rectangle_first, self.value_rectangle_second))

        self.clear_canvas_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Funções", menu=self.clear_canvas_menu)
        self.clear_canvas_menu.add_command(label="Apagar tudo", command=self.clear_canvas)

        # Configurar evento de clique no canvas
        self.canvas.bind("<Button-1>", self.get_coordinates)
        self.canvas.bind("<Button-2>", self.central_coords)
        self.canvas.bind("<Button-3>", self.get_coordinates_rectangle)
        self.window.mainloop()

    """
        Transforma os pontos existentes no canvas de acordo com a função de transformação fornecida
        e desenha os pontos transformados no canvas.

        Args:
            transformation_function: Função de transformação que recebe uma lista de pontos
                                    e retorna uma lista de pontos transformados.
    """
    def transform_and_drawn(self, transformation_function):
        points = self.canvas.find_all()
        existing_points = [(self.canvas.coords(point)[0], self.canvas.coords(point)[1]) for point in points]

        transformed_points = transformation_function(existing_points)

        self.clear_canvas()
        for x, y in transformed_points:
            self.canvas.create_oval(x, y, x + 1, y + 1, fill="black")

    """
        Define as coordenadas do ponto central para transformações de acordo com o evento de clique no canvas.

        Args:
            event: O evento do mouse contendo as coordenadas x e y do ponto clicado.
    """
    def central_coords(self, event):
        x = event.x
        y = event.y

        self.value_center_point = (x, y)
        self.center_point_text.set(f"Ponto origem selecionado: {self.value_center_point}")

    """
        Obtém as coordenadas dos pontos 1 e 2 para desenhar linhas de acordo com o evento de clique no canvas.

        Args:
            event: O evento do mouse contendo as coordenadas x e y do ponto clicado.
    """
    def get_coordinates(self, event):
        x = event.x
        y = event.y

        if self.point_count % 2 == 0:
            self.value_first_point = (x, y)
            self.first_point_text.set(f"Ponto 1: {self.value_first_point}")
        else:
            self.value_second_point = (x, y)
            self.second_point_text.set(f"Ponto 2: {self.value_second_point}")
        self.point_count += 1
    
    """
        Obtém as coordenadas dos pontos do retângulo para desenhar retângulos de acordo com o evento de clique no canvas.

        Args:
            event: O evento do mouse contendo as coordenadas x e y do ponto clicado.
    """
    def get_coordinates_rectangle(self, event):
        x = event.x
        y = event.y

        if self.rectangle_point_count % 2 == 0:
            self.value_rectangle_first = (x, y)
            self.rectangle_first_point_text.set(f"Ponto 1 do retângulo: {self.value_rectangle_first}")
        else:
            self.value_rectangle_second = (x, y)
            self.rectangle_second_point_text.set(f"Ponto 2 do retângulo: {self.value_rectangle_second}")
        self.rectangle_point_count += 1

    """
        Limpa o canvas, removendo todos os elementos desenhados.
    """
    def clear_canvas(self):
        self.canvas.delete("all")
