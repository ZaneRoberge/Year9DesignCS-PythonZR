
import tkinter as tk

root = tk.Tk()

photocanvas = tk.Canvas(root,width = 600, height = 600, background = "white")
photocanvas.grid(row = 0, column = 0, columnspan = 6)
photo=tk.PhotoImage(file ='math.jpeg')
photocanvas.create_image(50,10,image=photo,anchor = tk.NW)

root.mainloop()