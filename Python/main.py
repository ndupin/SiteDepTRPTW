#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:22:27 2017

@author: remimolette
"""
from constantes import constantes
import numpy as np
import pandas as pd
import sys
import ls_solver

def main(argv):

    if (len(argv)==0):
        instance_to_solve=range(0,125)
    elif ((len(argv)==1)):
        instance_to_solve=[int(argv[0])]
    elif ((len(argv)>1)):
        instance_to_solve=range(int(argv[0]),int(argv[1])+1)

    fichier = open("resultLocalSolver.csv", "w")

    for instance in instance_to_solve:    
            constantes.init(instance)
            print("CALCUL LOCALSOLVER instance : " + str(constantes.INSTANCE))
            obj= ls_solver.ls_prob.ls_problem(time_limit=constantes.LS_TIME_LIMIT)
            fichier.write(str(constantes.INSTANCE)+" ; "+ str(obj) + ";\n")
    fichier.close()

if __name__ == '__main__':
    main(sys.argv[1:])
print(" ")
