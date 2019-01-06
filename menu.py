from tkinter import *
import tkinter.font as tkFont
import pong
import parametres as paramWindow

pointer = "jouer"

tk = None
police = None
canvas = None
jouer = None
parametres = None

def binding(inputKey):

	print(2)

	global tk
	global pointer
	
	if inputKey.keysym == "q" or inputKey.keysym == "Q":
		pointer = "jouer"
		frame()

	if inputKey.keysym == "d" or inputKey.keysym == "D":
		pointer = "parametres"
		frame()

	if inputKey.keysym == "Return" and pointer == "jouer":
		tk.destroy()
		pong.start()

	if inputKey.keysym == "Return" and pointer == "parametres":
		tk.destroy()
		paramWindow.start()

def frame():

	global tk
	global canvas
	global parametres
	global jouer
	global police

	global pointer

	print(1)

	if(pointer == "jouer"):

		canvas.create_rectangle(0, 0, 500, 600, fill="#AEB6BF")
		jouer = canvas.create_text(250, 300, text="Jouer", font=police, fill='#17202A')
		canvas.create_rectangle(500, 0, 1000, 600, fill="#17202A")
		parametres = canvas.create_text(750, 300, text="Parametres", font=police, fill='#AEB6BF')

	else:

		canvas.create_rectangle(500, 0, 1000, 600, fill="#AEB6BF")
		parametres = canvas.create_text(750, 300, text="Parametres", font=police, fill='#1C2833')
		canvas.create_rectangle(0, 0, 500, 600, fill="#1C2833")
		jouer = canvas.create_text(250, 300, text="Jouer", font=police, fill='#AEB6BF')

def start():

	global tk
	global canvas
	global parametres
	global jouer
	global police

	tk = Tk()
	tk.bind_all('<Key>', binding)
	tk.title('Menu PONG')
	tk.resizable(0,0)
	canvas=Canvas(tk,width=1000,height=600)
	canvas.pack()
	police = tkFont.Font(family="Good Times", size=25)

	canvas.create_rectangle(0, 0, 500, 600, fill="#1C2833")
	canvas.create_rectangle(500, 0, 1000, 600, fill="#17202A")

	jouer = canvas.create_text(250, 300, text="Jouer", font=police, fill='#AEB6BF')
	parametres = canvas.create_text(750, 300, text="Parametres", font=police, fill='#AEB6BF')
	frame()
	tk.update()

	tk.mainloop()