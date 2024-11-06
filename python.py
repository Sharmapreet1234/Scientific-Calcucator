import tkinter as tk
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to insert text into entry
def insert_text(value):
    entry.insert(tk.END, value)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete last character
def backspace():
    current_text = entry.get()
    entry.delete(len(current_text)-1, tk.END)

# Function for trigonometric and logarithmic functions
def trig_log_function(func):
    try:
        value = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for square root and power functions
def special_function(func):
    try:
        value = float(entry.get())
        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "x^2":
            result = value ** 2
        elif func == "x^3":
            result = value ** 3
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Entry field
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons
button_texts = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '←',
    '1', '2', '3', '-', 'π',
    '0', '.', '+', '(', ')',
    'sin', 'cos', 'tan', 'log', 'ln',
    'x^2', 'x^3', 'sqrt', '^', '='
]

row_num = 1
col_num = 0

for text in button_texts:
    if text.isdigit() or text == '.':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda t=text: insert_text(t))
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=clear_entry)
    elif text == '←':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=backspace)
    elif text in ('+', '-', '*', '/', '(', ')', '^'):
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda t=text: insert_text(t))
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=evaluate_expression)
    elif text == 'sin':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: trig_log_function("sin"))
    elif text == 'cos':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: trig_log_function("cos"))
    elif text == 'tan':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: trig_log_function("tan"))
    elif text == 'log':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: trig_log_function("log"))
    elif text == 'ln':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: trig_log_function("ln"))
    elif text == 'sqrt':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: special_function("sqrt"))
    elif text == 'x^2':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: special_function("x^2"))
    elif text == 'x^3':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: special_function("x^3"))
    elif text == 'π':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: insert_text(str(math.pi)))

    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 4:
        col_num = 0
        row_num += 1

# Run the application
root.mainloop()
