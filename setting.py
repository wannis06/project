#import
from tkinter import *

#creeation de la fonction principale
def aff_setting(self):
    set = Tk()
    set.geometry('400x400')

    #creeation du menu pricipale
    menubar = Menu(set)
    set.config(menu = menubar)

    #fichier
    menufichier = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fichier", menu = menufichier)

    set.mainloop()

