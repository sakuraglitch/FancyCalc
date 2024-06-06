import tkinter as tk
from tkinter import ttk


class FancyCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fancy Calculator")
        self.geometry("350x450")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')  # 'clam', 'alt', 'default', 'classic'

        self.style.configure('TEntry',
                             foreground='white',
                             background='white',
                             fieldbackground='green',
                             font=("arial", 50))

        self.style.configure('TButton',
                             font=("Helvetica", 14, 'bold'),
                             padding=10,
                             foreground='white',
                             background='green',  # green background
                             borderwidth=1)

        self.style.map('TButton',
                       foreground=[('active', 'white')],
                       background=[('active', '#addf27')])  # lime green on active

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for display
        entry = ttk.Entry(self, textvariable=self.result_var, justify='right', style='TEntry')
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10, padx=10)

        # Button configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t), style='TButton')
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)


if __name__ == "__main__":
    calculator = FancyCalculator()
    calculator.mainloop()
