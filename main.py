#import de module
from tkinter import *
import os

#information logicielle
title = 'gestach'
version = 'alpha 0.1'
author = 'Yannis Legros'
description = ''

#creeation du fichier du logicielle dans les doc
def creat_file(username):
    os.mkdir(f'C:/Users/{username}/Documents/gestach')
#créeation des variable de base
master = Tk()
username = os.environ.get( "USERNAME" )

#creeation de la fenetre principale
master.geometry('920x720')

#boucle tkinter
master.mainloop()