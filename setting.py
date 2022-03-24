#import
from cgitb import text
from tkinter import *

#creeation de la fonction principale
def aff_setting():
    set = Tk()
    set.geometry('400x400')
    Label(set, text = 'setting', font = (0, 50)).pack()
    
    set.mainloop()