#import de module
from tkinter import *
import os
import setting

#information logicielle
title = 'gestach'
version = 'alpha 0.1'
author = 'Yannis Legros'
description = ''

#creeation des fonction du logicielle

#creeation du fichier du logicielle dans les doc
def creat_file(username):
    os.mkdir(f'C:/Users/{username}/Documents/gestach')


#créeation des variable de base
master = Tk()
username = os.environ.get( "USERNAME" )

#creeation de la fenetre principale
master.geometry('920x720')

#creeation du menu pricipale
menubar = Menu(master)
master.config(menu = menubar)

#fichier
menufichier = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu = menufichier)
menufichier.add_command(label = 'ouvrire')

#preference
menupreference = Menu(menubar, tearoff=0)
menubar.add_cascade(label = 'preference', menu = menupreference)
menupreference.add_command(label = 'setting', command = setting.aff_setting)

#boucle tkinter
master.mainloop()