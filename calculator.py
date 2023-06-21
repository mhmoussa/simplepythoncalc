import tkinter as tk
from tkinter import messagebox

# Define the color scheme
BG_COLOR = "#283149"  # Dark blue
BTN_BG_COLOR = "#394867"  # Blue-gray
BTN_FG_COLOR = "black"  # Updated to black
ENTRY_BG_COLOR = "#eeeeee"  # Light gray
ENTRY_FG_COLOR = "black"

# Calculate the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear the entry field
def clear():
    entry.delete(0, tk.END)

# Add a value to the entry field
def add_to_entry(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

# Add the current value to memory
def add_memory():
    value = entry.get()
    memory.append(value)
    messagebox.showinfo("Memory", "Value added to memory.")

# Recall the last value from memory
def recall_memory():
    if memory:
        value = memory[-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)
        messagebox.showinfo("Memory", "Value recalled from memory.")
    else:
        messagebox.showinfo("Memory", "Memory is empty.")

# Clear the memory
def clear_memory():
    memory.clear()
    messagebox.showinfo("Memory", "Memory cleared.")

# Handle keypress events
def handle_keypress(event):
    if event.keysym == "Return":
        calculate()

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(background=BG_COLOR)

# Create an entry field
entry = tk.Entry(window, width=30, justify=tk.RIGHT, bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "sqr", "C",
    "M+", "MR", "MC"
]

row = 1
column = 0

memory = []

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=calculate).grid(row=row, column=column, padx=5, pady=5)
    elif button == "C":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=clear).grid(row=row, column=column, padx=5, pady=5)
    elif button == "sqr":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=lambda: add_to_entry("**2")).grid(row=row, column=column, padx=5, pady=5)
    elif button == "M+":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=add_memory).grid(row=row, column=column, padx=5, pady=5)
    elif button == "MR":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=recall_memory).grid(row=row, column=column, padx=5, pady=5)
    elif button == "MC":
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=clear_memory).grid(row=row, column=column, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=7, bg=BTN_BG_COLOR, fg=BTN_FG_COLOR, command=lambda value=button: add_to_entry(value)).grid(row=row, column=column, padx=5, pady=5)

    column += 1

    if column > 3:
        column = 0
        row += 1

# Bind Enter keypress to the calculate function
window.bind("<KeyPress>", handle_keypress)

# Add copyright notice and email
copywrite_label = tk.Label(window, text="\u00A9 Mohammad Moussa | me@mhmoussa.com", font=("Arial", 10), bg=BG_COLOR, fg=ENTRY_FG_COLOR)
copywrite_label.grid(row=row, column=0, columnspan=4, padx=10, pady=10)

# Run the main event loop
window.mainloop()
