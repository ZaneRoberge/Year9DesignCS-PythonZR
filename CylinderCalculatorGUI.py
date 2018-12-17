
import tkinter as tk

root = tk.Tk()


titleLabel = tk.Label(root , text = "math calc", font=("Helvetica", 70))


titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

word1Label = tk.Label(root, text = "Formula", background = "beige", foreground = "black")
word1Label.grid(row = 2, column = 0)

word2Label = tk.Label(root, text = "  Entry  ", background = "beige", foreground = "black")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = " output ", background = "beige", foreground = "black")
word3Label.grid(row = 4, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)












root.mainloop()