from tkinter import *
import tkinter.font as tkFont
import menu
import pickle

couleur_balle = None
couleur_raquette_droite = None
couleur_raquette_gauche = None
couleur_arriere_plant = None
vitesse_balle = None
limite_points = None

tk = None
input_limite_points = None
input_couleur_raquette_gauche = None
input_couleur_raquette_droite = None
input_couleur_balle = None
input_vitesse_balle = None
input_couleur_arriere_plant = None

def save():

	global couleur_balle
	global couleur_raquette_droite
	global couleur_raquette_gauche
	global couleur_arriere_plant
	global vitesse_balle
	global limite_points

	global tk
	global input_limite_points
	global input_couleur_raquette_gauche
	global input_couleur_raquette_droite
	global input_couleur_balle
	global input_vitesse_balle
	global input_couleur_arriere_plant

	couleur_balle = input_couleur_balle.get()
	couleur_raquette_droite = input_couleur_raquette_droite.get()
	couleur_raquette_gauche = input_couleur_raquette_gauche.get()
	couleur_arriere_plant = input_couleur_arriere_plant.get()
	vitesse_balle = input_vitesse_balle.get()
	limite_points = input_limite_points.get()

	if (couleur_arriere_plant == "" or couleur_arriere_plant == None):
		couleur_arriere_plant = "#1C2833"

	if (couleur_balle == "" or couleur_balle == None):
		couleur_balle = "#fff"

	if (couleur_raquette_gauche == "" or couleur_raquette_gauche == None):
		couleur_raquette_gauche = "#fff"

	if (couleur_raquette_droite == "" or couleur_raquette_droite == None):
		couleur_raquette_droite = "#fff"

	if (vitesse_balle == "" or vitesse_balle == None):
		vitesse_balle = 2

	if (limite_points == "" or limite_points == None):
		limite_points = 8

	with open('settings.pkl', 'wb') as settingsWrite:
		pickle.dump([couleur_balle, couleur_raquette_droite, couleur_raquette_gauche, couleur_arriere_plant, vitesse_balle, limite_points], settingsWrite)

	with open('settings.pkl', 'rb') as settingsFile:
	    print(pickle.load(settingsFile))

	tk.destroy()
	menu.start()

def raz():

	global input_limite_points
	global input_couleur_raquette_gauche
	global input_couleur_raquette_droite
	global input_couleur_balle
	global input_vitesse_balle
	global input_couleur_arriere_plant

	input_limite_points.delete(0, END)
	input_couleur_raquette_gauche.delete(0, END)
	input_couleur_raquette_droite.delete(0, END)
	input_couleur_balle.delete(0, END)
	input_vitesse_balle.delete(0, END)
	input_couleur_arriere_plant.delete(0, END)

	input_limite_points.insert(END, 8)
	input_couleur_raquette_gauche.insert(END, "#fff")
	input_couleur_raquette_droite.insert(END, "#fff")
	input_couleur_balle.insert(END, "#fff")
	input_vitesse_balle.insert(END, 2)
	input_couleur_arriere_plant.insert(END, "#1C2833")

def start():

	global couleur_balle
	global couleur_raquette_droite
	global couleur_raquette_gauche
	global couleur_arriere_plant
	global vitesse_balle
	global limite_points

	with open('settings.pkl', 'rb') as settingsFile:
	    couleur_balle, couleur_raquette_droite, couleur_raquette_gauche, couleur_arriere_plant, vitesse_balle, limite_points = pickle.load(settingsFile)

	global tk
	global input_limite_points
	global input_couleur_raquette_gauche
	global input_couleur_raquette_droite
	global input_couleur_balle
	global input_vitesse_balle
	global input_couleur_arriere_plant

	tk = Tk()
	tk.title("parametres PONG")
	police = tkFont.Font(family="Good Times", size=16)

	titre_limite_points = Label(tk, text="Points :", font=police)
	titre_limite_points.grid(column=0, row=0, padx=20, pady=5)

	input_limite_points = Entry(tk, font=police)
	input_limite_points.insert(END, limite_points)
	input_limite_points.grid(column=1, row=0, padx=20, pady=5)

	titre_couleur_raquette_gauche = Label(tk, text="Couleur Raquette Gauche :", font=police)
	titre_couleur_raquette_gauche.grid(column=0, row=1, padx=20, pady=5)

	input_couleur_raquette_gauche = Entry(tk, font=police)
	input_couleur_raquette_gauche.insert(END, couleur_balle)
	input_couleur_raquette_gauche.grid(column=1, row=1, padx=20, pady=5)

	titre_couleur_raquette_droite = Label(tk, text="Couleur Raquette Droite :", font=police)
	titre_couleur_raquette_droite.grid(column=0, row=2, padx=20, pady=5)

	input_couleur_raquette_droite = Entry(tk, font=police)
	input_couleur_raquette_droite.insert(END, couleur_raquette_droite)
	input_couleur_raquette_droite.grid(column=1, row=2, padx=20, pady=5)

	titre_couleur_balle = Label(tk, text="Couleur balle :", font=police)
	titre_couleur_balle.grid(column=0, row=3, padx=20, pady=5)

	input_couleur_balle = Entry(tk, font=police)
	input_couleur_balle.insert(END, couleur_balle)
	input_couleur_balle.grid(column=1, row=3, padx=20, pady=5)

	titre_vitesse_balle = Label(tk, text="Vitesse balle :", font=police)
	titre_vitesse_balle.grid(column=0, row=4, padx=20, pady=5)

	input_vitesse_balle = Entry(tk, font=police)
	input_vitesse_balle.insert(END, vitesse_balle)
	input_vitesse_balle.grid(column=1, row=4, padx=20, pady=5)

	titre_couleur_arriere_plant = Label(tk, text="Couleur arriere plant :", font=police)
	titre_couleur_arriere_plant.grid(column=0, row=5, padx=20, pady=5)

	input_couleur_arriere_plant = Entry(tk, font=police)
	input_couleur_arriere_plant.insert(END, couleur_arriere_plant)
	input_couleur_arriere_plant.grid(column=1, row=5, padx=20, pady=5)

	boutton_valider = Button(text="Valider", font=police, command=save)
	boutton_valider.grid(column=1, row=6, padx=20, pady=5)

	bouttoin_reset = Button(text="RAZ", font=police, command=raz)
	bouttoin_reset.grid(column=0, row=6, padx=20, pady=5)

	tk.mainloop()