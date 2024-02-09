#simple addition window using tkinter 

import tkinter as tk

def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 + num2)

def subtract_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 - num2)

root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
result = tk.StringVar()

tk.Label(root, text="Enter Number 1:").pack()
entry1.pack()

tk.Label(root, text="Enter Number 2:").pack()
entry2.pack()

tk.Button(root, text="Add", command=add_numbers).pack(side=tk.LEFT)
tk.Button(root, text="Subtract", command=subtract_numbers).pack(side=tk.RIGHT)

tk.Label(root, text="Result:").pack()
tk.Label(root, textvariable=result).pack()

root.mainloop()
