from tkinter import *
import tkinter.font as tkFont
import pickle

temps = None
score_droite = None
score_gauche = None
gagant = None

def start():

	global temps
	global score_droite
	global score_gauche
	global gagant

	with open('scoreboard.pkl', 'rb') as f:
		temps, score_gauche, score_droite = pickle.load(f)

	tk= Tk()

	tk.title("SCOREBOARD PONG")
	tk.resizable(0,0)

	canvas = Canvas(tk, width = 1000, height=600, bg="#000")
	canvas.pack()

	if(score_droite > score_gauche):
		gagant = "droite"
	else:
		gagant = "gauche"

	police = tkFont.Font(family="Good Times", size=24)

	canvas.create_text(1000/2, 600 * (1/6), text="Le gagnant est le joueur de "+gagant, font= police, fill="white")
	canvas.create_text(1000 * (1/3), 600/2, text=score_gauche, font= police, fill="white")
	canvas.create_text(1000 * (2/3), 600/2, text=score_droite, font= police, fill="white")
	canvas.create_text(1000/2, 600 * (5/6), text=str(int(temps))+" '", font= police, fill="white")