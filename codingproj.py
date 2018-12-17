
import tkinter as tk

root = tk.Tk()

root.config(background = "grey")


titleLabel = tk.Label(root , text = "Formulator", font=("Helvetica", 30), background = "light grey" )


titleLabel.grid(row = 0, column = 0, columnspan = 2)



word1Label = tk.Label(root, text = "SlopeFormula",  foreground = "black", font=("Arial", 15), background = "light grey")
word1Label.grid(row = 1, column = 1)

word2Label = tk.Label(root, text = "  entry  ", foreground = "black", background = "light grey")
word2Label.grid(row = 5, column = 0)

word3Label = tk.Label(root, text = " output ", foreground = "black", background = "light grey")
word3Label.grid(row = 6, column = 0)

word4Label = tk.Label(root, text = "m = y2 - y1 / x2 - x1",  font=("Arial", 15), background = "light grey")
word4Label.grid(row = 2, column = 1)





def callbacksf():
	word1Label.config (text = "SlopeFormula")
	word4Label.config (text = "m = y2 - y1 / x2 - x1")
	data [0] = 0

	
def callbackmp():
	word1Label.config (text = "Midpoint")
	word4Label.config (text = "M((x1+x2)/2,(y1+y2)/2)")
	data[0] = 1

def callbacklol():
	word1Label.config (text = "length of a line")
	word4Label.config (text = "D = √(x2−x1)*2+(y2−y1)*2")
	data[0] = 2

def runme():
	print(data[0])
	#Get my data
	entryData = ent2.get()
	print(entryData)
	x1 = int(entryData[0])
	y1 = int(entryData[2])
	x2 = int(entryData[4])
	y2 = int(entryData[6])
	if data[0] == 0:
		print("slope")
		ent2.delete(0,tk.END)
		m = (y2-y1)/(x2-x1)
		ent3.delete(0,tk.END)
		ent3.insert(tk.END,"The slope is "+str(m))
	if data[0] == 1:
		x1 = int(entryData[0])
		x2 = int(entryData[2])
		y1 = int(entryData[4])
		y2 = int(entryData[6])
		print("midpoint")
		ent2.delete(0,tk.END)
		m = ((x1+x2)/2,(y1-y2)/2)
		ent3.delete(0, tk.END)
		ent3.insert(tk.END, "The midpoint is "+str(m))


data = [0]#data stores the current button selected data[0] = 0 slope data[0] = 1 midpoint data[0] = 1 length




ent2 = tk.Entry(root, background = "light grey")
ent2.grid(row = 5, column = 1)

ent3 = tk.Entry(root, background = "light grey")
ent3.grid(row = 6, column = 1)

btn1 = tk.Button(root, text = "SlopeFormula", command = callbacksf, background = "grey")
btn1.grid(row = 1, column = 0 )

btn2 = tk.Button(root, text = "Midpoint", font=25, command = callbackmp, background = "grey")
btn2.grid(row = 2, column = 0 )

btn3 = tk.Button(root, text = "length of a line", command = callbacklol, background = "grey")
btn3.grid(row = 3, column = 0 )

btn4 = tk.Button(root, text = "submit", background = "grey", padx = 20, pady = 10, command = runme)
btn4.grid(row = 8, column = 1)












root.mainloop()