import tkinter as tk

# ---------------- Functions ----------------

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="x", padx=10, pady=10)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 16),
                            command=calculate)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 16),
                            command=lambda c=char: press(c))

        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 16), command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
