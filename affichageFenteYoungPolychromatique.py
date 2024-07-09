# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:54:48 2023

@author: alexa
"""

import tkinter as tk
from math import cos,pi, exp
import numpy as np

def _from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def affichage(long_onde,a,d,rb,expe=False):
    fenetre = tk.Tk()
    canvas = tk.Canvas(fenetre, width=1000, height=120, background='black')
    lst_couleurs = [(0,0,0) for i in range(1002)]
    somme = somme2(long_onde)
    for lo in long_onde :
       l, i = lo
       trous_young(lst_couleurs,l,i,a,d,rb,somme,expe)
       trans_entier(lst_couleurs)
    for i in range(1002) :
        canvas.create_line(i, 0, i, 122,fill = _from_rgb(lst_couleurs[i]))
    canvas.pack()
    fenetre.mainloop()
    
def trous_young(lst,lo,i,a,d,rb,nb_lo,expe):
    for x in range(len(lst)):
        nlo = lo*10E-5
        L = 2*d*nlo/rb
        xut = x-500
        intens = 0.5*i*(1 + cos(2*pi*a*xut/(nlo*d)))
        intens *= exp(-(xut)*(xut)/((L/2)*(L/2)))
        if expe :
            r, g, b = conv_exp_lo_to_rgb(lo)
        else :
            r, g, b = conv_lo_to_rgb(lo)
        lst[x] = (lst[x][0]+(intens*r)/nb_lo, lst[x][1]+(intens*g)/nb_lo, lst[x][2]+(intens*b)/nb_lo)
        
def trans_entier(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i][0]),int(lst[i][1]),int(lst[i][2])

def somme2(lst):
    acc = 0
    for lo in lst :
        l, i = lo
        acc += i
    return acc
    
def ouvrir_fichier(file):
    lst = np.loadtxt(file, delimiter = ' ')
    return lst

def conv_lo_to_rgb(lo):
    lst = file1[lo-380]
    return int(lst[1]*255),int(lst[2]*255),int(lst[3]*255)

def conv_exp_lo_to_rgb(lo):
    for lst in file2 :
        if lst[0] == lo :
            return lst[1],lst[2],lst[3]

def f(i):
    h = 6.62e-34
    c = 299792458
    nu = c/i
    k = 1.38e-23
    T = 5000
    return (2*h*nu**3/c**2)/(exp(h*nu/k*T)-1)
 
file1 = ouvrir_fichier("Valeur theoriques.txt")
file2 = ouvrir_fichier("ValeursExperimentales.txt")
affichage([(436,1),(468,1),(480,1),(509,1),(546,1),(577,1),(579,1),(644,1)],10,10000,2,True) #mercure cadmium expérimentale
affichage([(436,1),(468,1),(480,1),(509,1),(546,1),(577,1),(579,1),(644,1)],10,10000,2) #mercure cadmium valeurs réelles
affichage([(i,1) for i in range(380,780,20)],10,10000,2,False) #lumière blanche équirépartie
affichage([(i,f(i)) for i in range(380,780,20)],10,10000,2,False) #lumière blance avec loi de Planck
#en 10E-4 m