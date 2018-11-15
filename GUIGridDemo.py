import tkinter as tk

root = tk.Tk()




ent = tk.Entry(root)
ent.grid(row = 0, column = 0)


btn = tk.Button(root, text = "Press Me")
btn.grid(row = 100, column = 100)




label = tk.Label(root, text = "...")


root.mainloop()
