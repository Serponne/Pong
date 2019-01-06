from tkinter import *
import time
import random
import tkinter.font as tkFont
import pickle
import scoreboard

couleur_balle = None
couleur_raquette_droite = None
couleur_raquette_gauche = None
couleur_arriere_plant = None
vitesse_balle = None
limite_points = None

temps = 0
score_droite = 0
score_gauche = 0

with open('settings.pkl', 'rb') as settingsFile:
    couleur_balle, couleur_raquette_droite, couleur_raquette_gauche, couleur_arriere_plant, vitesse_balle, limite_points = pickle.load(settingsFile)

tk = None
canvas = None
text_score_gauche = None
text_score_droite = None
police = None

ball = None
raquette_gauche = None
raquette_droite = None

limite_score = None


class Ball:
    """docstring for Ball"""
    def __init__(self, canvas, color):

        global vitesse_balle

        self.x= int(vitesse_balle)
        self.y= int(vitesse_balle)
        self.canvas = canvas
        self.id = canvas.create_oval (self.canvas.winfo_width()/2-10,self.canvas.winfo_height()/2-10,self.canvas.winfo_width()/2+10,self.canvas.winfo_height()/2+10, fill = color, width=0)



    def position(self):
        pos_ball = self.canvas.coords(self.id)
        return pos_ball



    def draw(self):

        global score_gauche
        global score_droite

        pos_ball =  self.position()

        ###############  GESTION DES COLLISIONS ##################

        ############### Collisions murs ##########################
        if (pos_ball[0] <= 0):
            score_droite+=1
            self.centrer()
            rand = random.randint(1, 2)
            self.x = int(vitesse_balle)
            self.y = int(vitesse_balle)

            if(rand == 1):
                self.y *= -1

        if (pos_ball[1] <= 0 ):
            self.y = self.y * -1

        if (pos_ball[2] >= 1000):
            score_gauche+=1
            self.centrer()
            rand = random.randint(1, 2)
            self.x = int(vitesse_balle) * -1
            self.y = int(vitesse_balle)

            if(rand == 1):
                self.y *= -1

        if (pos_ball[3] >= 600):
            self.y = self.y * -1
        

        self.canvas.move(self.id,self.x,self.y)

    def centrer(self):

        self.canvas.coords(self.id, 1000/2-10,600/2-10,1000/2+10,600/2+10)


class Raquette:

    def __init__(self, canvas, color, position):
        self.canvas = canvas
        self.yhaut = -32
        self.ybas = 32
        self.position = position
        self.id = self.canvas.create_rectangle(position-5, 300-40, position+5, 300+40, fill=color, width=0)

    def move_haut(self):
        self.canvas.move(self.id, 0, self.yhaut)

    def move_bas(self):
        self.canvas.move(self.id, 0, self.ybas)

    def position_haut(self):
        return self.canvas.coords(self.id)[1]

    def position_bas(self):
        return self.canvas.coords(self.id)[3]

    def draw(self):
         
        if(self.position_haut() < 0):
            self.move_bas()

        if(self.position_bas() > 600):
            self.move_haut()


def touche_clavier(inputKey):

    global raquette_droite
    global raquette_gauche

    global ball
    global raquette_gauche
    global raquette_droite
    
    if inputKey.keysym == "Up":
        raquette_droite.move_haut()
    if inputKey.keysym == "Down":
        raquette_droite.move_bas()

    if inputKey.keysym == "s" or inputKey.keysym == "S":
        raquette_gauche.move_haut()
    if inputKey.keysym == "x" or inputKey.keysym == "X":
        raquette_gauche.move_bas()

def ecran_fin():

    global tk
    global temps
    global score_gauche
    global score_droite

    temps = int(round(temps * 0.034, 0))

    with open('scoreboard.pkl', 'wb') as scoreFile:
        pickle.dump([temps, score_gauche, score_droite], scoreFile)


    scoreboard.start()
    tk.destroy()


def frame():

    global temps
    global score_droite
    global score_gauche

    temps += 1

    global canvas

    global raquette_droite
    global raquette_gauche

    global ball

    global tk
    global police
    global text_score_droite
    global text_score_gauche

    if score_droite == limite_score or score_gauche == limite_score:
        tk.destroy()
        ecran_fin()

    ball.draw()
    raquette_gauche.draw()
    raquette_droite.draw()

    #########COLLISION RAQUETTES########
    #GAUCHE#
    if (ball.position()[0] <= 85 and ball.position()[0] >= 65):
        if(ball.position()[1]+10 <= raquette_gauche.position_bas() and ball.position()[1]+10 >= raquette_gauche.position_haut()):
            ball.x *= 1.05
            ball.y *= 1.05
            ball.x = ball.x * -1

    #DROITE#
    if (ball.position()[2] >= 915 and ball.position()[2] <= 935):
        if(ball.position()[3]-10 >= raquette_droite.position_haut() and ball.position()[3]-10 <= raquette_droite.position_bas()):
            ball.x *= 1.05
            ball.y *= 1.05
            ball.x = ball.x * -1

    ##########AFFICHAGE SCORE######

    canvas.delete(text_score_gauche)
    text_score_gauche = canvas.create_text(37.5, 50, text=str(score_gauche), font=police, fill='#AEB6BF')

    canvas.delete(text_score_droite)
    text_score_droite = canvas.create_text(925 + 37.5, 50, text=str(score_droite), font=police, fill='#AEB6BF')


    tk.after(17,frame)

def start():

    global limite_score
    global couleur_balle
    global couleur_raquette_droite
    global couleur_raquette_gauche
    global couleur_arriere_plant
    global vitesse_balle
    global limite_points

    global police
    global raquette_droite
    global raquette_gauche

    global text_score_droite
    global text_score_gauche

    global ball

    global canvas
    global tk

    with open('settings.pkl', 'rb') as settingsFile:
        couleur_balle, couleur_raquette_droite, couleur_raquette_gauche, couleur_arriere_plant, vitesse_balle, limite_points = pickle.load(settingsFile)

    limite_score = int(limite_points)

    tk= Tk()

    tk.title("PONG")
    tk.resizable(0,0)

    canvas = Canvas(tk, width = 1000, height=600, bg=couleur_arriere_plant)
    canvas.pack()

    canvas.create_line(75,0,75,600, fill='grey', dash=(1, 3))
    canvas.create_line(925,0,925,600, fill='grey', dash=(1, 3))
    canvas.create_line(500, 0, 500, 600, fill='#17202A')

    tk.bind_all("<Key>", touche_clavier)

    raquette_gauche = Raquette(canvas, couleur_raquette_gauche, 75)
    raquette_droite = Raquette(canvas, couleur_raquette_droite, 925)

    police = tkFont.Font(family="Good Times", size=25)
    text_score_gauche = canvas.create_text(37.5, 50, text=str(score_gauche), font=police, fill='#AEB6BF')
    text_score_droite = canvas.create_text(925 + 37.5, 50, text=str(score_droite), font=police, fill='#AEB6BF')

    tk.update()

    ball= Ball(canvas, couleur_balle)

    frame()

    tk.mainloop()