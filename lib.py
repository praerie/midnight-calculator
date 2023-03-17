import math
import calculator as gui
import const as c


exp = ""


def add_to_exp(button_press):
    """adds each char to str 'exp' when buttons pressed"""
    global exp

    if button_press != ".":
        remove_leading_zero()

    exp += str(button_press)

    gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
    gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)


def evaluate_exp():
    """when equal button pressed, evaluates expression"""
    global exp

    if "%" in exp:
        calculate_modulus()
    else:
        try:
            exp = str(eval(exp))
            exp = clear_decimal()

            gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
            gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)
        except:
            clear_input_field()
            gui.Calculator.update_input_field(gui.Calculator, c.insert, c.error_msg)


def evaluate_square_root():
    """calculates square root of a number or expression"""
    global exp

    if exp == None:
        gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
        gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)
    else:
        try:
            if "." in exp:
                exp = math.sqrt(float(exp))
            else:
                exp = math.sqrt(int(exp))

            exp = clear_decimal()

            gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
            gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)

            exp = str(exp)
        except:
            clear_input_field()
            gui.Calculator.update_input_field(gui.Calculator, c.insert, c.error_msg)


def clear_decimal():
    """converts 'n.0' to 'n' to remove unnecessary decimal"""
    global exp

    if str(exp).endswith(".0"):
        exp = round(float(exp))
        return exp
    else:
        return exp


def remove_leading_zero():
    """removes leading zero in input field"""
    global exp

    exp = str(exp)

    if len(exp) == 1 and exp[0] == "0":
        exp = exp[1:]


def calculate_modulus():
    """calculates modulus of 2 values a and b,
    first evaluating expressions and converting to whole number"""
    global exp

    try:
        a, b = exp.split("%", 1)
        a, b = str(eval(a)), str(eval(b))
        a, b = round(float(a)), round(float(b))
        a, b = abs(int(a)), abs(int(b))

        exp = math.fmod(a, b)
        exp = math.trunc(exp)

        gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
        gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)

        exp = str(exp)
    except:
        clear_input_field()
        gui.Calculator.update_input_field(gui.Calculator, c.insert, c.error_msg)


def clear_input_field():
    """deletes all characters in text box"""
    global exp

    exp = ""
    gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)


def clear_last_char():
    """deletes only last entered character in text box"""
    global exp

    exp = exp[:-1]
    gui.Calculator.update_input_field(gui.Calculator, c.delete, c.end)
    gui.Calculator.update_input_field(gui.Calculator, c.insert, exp)
