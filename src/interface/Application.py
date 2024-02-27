class Application:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Definir o tamanho inicial da janela e centralizá-la na tela
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        initial_width = int(screen_width * 0.9)
        initial_height = int(screen_height * 0.9)
        x = (screen_width - initial_width) // 2
        y = (screen_height - initial_height) // 2
        self.window.geometry(f"{initial_width}x{initial_height}+{x}+{y}")

        self.window.mainloop()