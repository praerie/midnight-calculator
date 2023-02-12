import tkinter as tk
from buttons import Buttons
import const as c


class Calculator:
    root = tk.Tk()
    root.title(c.title)
    root.geometry(c.window_size)
    root.resizable(0, 0)

    input_field = tk.Text(root, height=4, width=20, font=c.input_font, bg=c.input_bg, fg=c.input_fg)
    input_field.grid(row=1, column=0, columnspan=4, sticky="nsew")

    buttons = Buttons(root)

    def update_input_field(self, action, content):
        if action == c.insert:
            self.input_field.insert(1.0, content)
        elif action == c.delete:
            self.input_field.delete(1.0, content)

    def begin(self):
        self.root.mainloop()
