import tkinter as tk

class Application:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Definir o tamanho inicial da janela e centralizá-la na tela
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        initial_width = int(screen_width * 0.7)
        initial_height = int(screen_height * 0.7)
        canvas_width = int(screen_width * 0.5)
        canvas_height = int(screen_height * 0.5)
        x = (screen_width - initial_width) // 2
        y = (screen_height - initial_height) // 2
        self.window.geometry(f"{initial_width}x{initial_height}+{x}+{y}")

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

        # Inicializar variáveis importantes
        self.value_first_point = None
        self.value_second_point = None
        self.point_count = 0

        # Configurar evento de clique no canvas
        self.canvas.bind("<Button-1>", self.get_coordinates)

        self.window.mainloop()

    '''
        Evento de pegar clique no canvas e setar os pontos selecionados.
        O primeiro clique preenche valores da variavel value_first_point
        o segundo preenche value_second_point e os próximos cliques seguem
        a ordem value_first_point -> value_second_point.
    '''
    def get_coordinates(self, event):
        x = event.x - self.canvas.winfo_width()/2
        y = -1 * (event.y - self.canvas.winfo_height()/2)

        if self.point_count % 2 == 0:
            self.value_first_point = (x, y)
            self.first_point_text.set(f"Ponto 1: {self.value_first_point}")
        else:
            self.value_second_point = (x, y)
            self.second_point_text.set(f"Ponto 2: {self.value_second_point}")
        self.point_count += 1