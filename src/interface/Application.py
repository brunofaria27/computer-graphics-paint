import tkinter as tk

from interface.FunctionsCaller import FunctionsCaller

class Application:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Definir o tamanho inicial da janela e canvas e centralizá-la na tela
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        initial_width = int(screen_width * 0.7)
        initial_height = int(screen_height * 0.8)
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

        self.dx_label = tk.Label(self.dx_translate, text="DX Translate:")
        self.dx_label.grid(row=1, column=0)
        self.dx_scale = tk.Scale(self.dx_translate, from_=1, to=200, orient=tk.HORIZONTAL)
        self.dx_scale.grid(row=1, column=1)

        self.dy_label = tk.Label(self.dy_translate, text="DY Translate:")
        self.dy_label.grid(row=1, column=0)
        self.dy_scale = tk.Scale(self.dy_translate, from_=1, to=200, orient=tk.HORIZONTAL)
        self.dy_scale.grid(row=1, column=1)

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
        self.transformation_menu.add_command(label="Translação", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))
        self.transformation_menu.add_command(label="Rotação", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))
        self.transformation_menu.add_command(label="Escala", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))
        self.transformation_menu.add_command(label="Reflexâo X", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))
        self.transformation_menu.add_command(label="Reflexâo Y", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))
        self.transformation_menu.add_command(label="Reflexâo XY", command=lambda: functions_caller.transform_and_drawn(self.canvas, ))

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
        Evento para pegar o ponto origem que será utilizado para as 
        funções de transformação no decorrer da interface.
    """
    def central_coords(self, event):
        x = event.x
        y = event.y

        self.value_center_point = (x, y)
        self.center_point_text.set(f"Ponto origem selecionado: {self.value_center_point}")

    '''
        Evento de pegar clique no canvas e setar os pontos selecionados.
        O primeiro clique preenche valores da variavel value_first_point
        o segundo preenche value_second_point e os próximos cliques seguem
        a ordem value_first_point -> value_second_point.
    '''
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
    
    '''
        Evento de pegar clique no canvas e setar os pontos selecionados.
        O primeiro clique preenche valores da variavel value_rectangle_first
        o segundo preenche value_rectangle_second e os próximos cliques seguem
        a ordem value_rectangle_first -> value_rectangle_second.
    '''
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

    '''
        Função usada para limpar toda a tela de desenhos feita pelo
        usuário.
    '''
    def clear_canvas(self):
        self.canvas.delete("all")
