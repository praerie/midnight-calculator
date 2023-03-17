import tkinter as tk
from lib import add_to_exp, evaluate_exp, evaluate_square_root, clear_input_field, clear_last_char
import const as c


class Buttons:
    def __init__(self, root):
        # create button to clear all
        btn_clear_input = tk.Button(root, text=c.clear_msg, command=clear_input_field,
                                    font=c.btn_font, bg=c.light_btn_bg, fg=c.clear_fg, height=2, borderwidth=0,
                                    activebackground=c.clear_active_bg, activeforeground=c.clear_active_fg)
        btn_clear_input.grid(row=2, column=0, columnspan=4, sticky="nsew")

        # create button to clear last char
        btn_clear_input = tk.Button(root, text=c.clear_arrow, command=clear_last_char,
                                    font=c.btn_font, bg=c.light_btn_bg, fg=c.clear_fg, height=2, borderwidth=0,
                                    activebackground=c.clear_active_bg, activeforeground=c.clear_active_fg)
        btn_clear_input.grid(row=7, column=0, sticky="nsew")

        # create digit buttons (digit, row, column)
        digits = [(7, 4, 0), (8, 4, 1), (9, 4, 2),
                  (4, 5, 0), (5, 5, 1), (6, 5, 2),
                  (1, 6, 0), (2, 6, 1), (3, 6, 2),
                  (0, 7, 1)]
        for i in digits:
            btn = tk.Button(root, text=i[0], command=lambda j=i[0]: add_to_exp(j),
                            font=c.btn_font, bg=c.input_bg, fg=c.digits_fg, height=2, borderwidth=0,
                            activebackground=c.digits_active_bg, activeforeground=c.digits_active_fg)
            btn.grid(row=i[1], column=i[2], sticky="nsew")

        # create symbol buttons (symbol, row, column)
        symbols = [("(", 3, 0), (")", 3, 1), ("%", 3, 2),
                   ("/", 3, 3), ("*", 4, 3),
                   ("-", 5, 3), ("+", 6, 3),
                   (".", 7, 2)]
        for i in symbols:
            btn = tk.Button(root, text=i[0], command=lambda j=i[0]: add_to_exp(j),
                            font=c.btn_font, bg=c.input_bg, fg=c.symbols_fg, height=2, borderwidth=0,
                            activebackground=c.symbols_active_bg, activeforeground=c.symbols_active_fg)
            btn.grid(row=i[1], column=i[2], sticky="nsew")

        # create square root button
        btn_square_root = tk.Button(root, text="√", command=evaluate_square_root,
                                    font=c.btn_font, bg=c.input_bg, fg=c.symbols_fg, height=2, borderwidth=0,
                                    activebackground=c.symbols_active_bg, activeforeground=c.symbols_active_fg)
        btn_square_root.grid(row=7, column=3, columnspan=1, sticky="nsew")

        # create equal button
        btn_clear_input = tk.Button(root, text="=", command=evaluate_exp,
                                    font=c.btn_font, bg=c.light_btn_bg, fg=c.clear_fg, height=2, borderwidth=0,
                                    activebackground=c.equals_active_bg, activeforeground=c.equals_active_fg)
        btn_clear_input.grid(row=8, column=0, columnspan=4, sticky="nsew")
