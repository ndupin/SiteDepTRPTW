#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:18:53 2017

@author: remimolette
"""
import time
import csv
from constantes import constantes
import os
import logging

class logger:
    previous_header = ""
    @staticmethod
    def log_csv(path = "./result/solution_log/",data = [], dual = {'PI':{}, 'sigma':{}},gl = False):
        ##nouveau path
        path1 = path +constantes.LISTE_INSTANCE[constantes.NUM_INSTANCE]+"/"
        if not os.path.exists(path1):
            os.makedirs(path1)
        path2 = path1+constantes.header_time+constantes.LISTE_INSTANCE[constantes.NUM_INSTANCE]+'_'+constantes.strat+'_log.csv'
#######################################ecriture de l'entete####################
        #ecriture d'unheader ou pas
        if(constantes.header_time != logger.previous_header):
            logger.previous_header = constantes.header_time
            ##casd'une generation de colonnes
            if gl==False:
               ##on ajoute les data qui sont sousforme d'un tableau
                row = ["time1", "time2","gl_name","obj_int"]  
                ##on ajoute les valeurs duales qui sous la forme d'un dictionnaire de dictionnaire
                pi = dual['PI']
                for k in range(1, len(pi)+1):
                    row.append("PI_"+str(k))
                sigma = dual['sigma']
                for k in range(1, len(sigma)+1):
                    row.append("sigma_"+str(k))
            ##cas d'un glouton
            else:
                row = ["time1", "time2", "obj_int"]  
            ##ecriture
            with open(path2, 'a') as f:
                w = csv.writer(f)
                w.writerow(row)  
  
########################################ecriture du corps du texte#############
        
        ##on ajoute les data qui sont sousforme d'un tableau
        ##casd'une generation de colonnes
        if gl==False:
            row = [time.ctime(), time.time()]+data   
            ##on ajoute les valeurs duales qui sous la forme d'un dictionnaire de dictionnaire
            pi = dual['PI']
            for k in range(1, len(pi)+1):
                row.append(pi[k])
            sigma = dual['sigma']
            for k in range(1, len(sigma)+1):
                row.append(sigma[k])
        ##cas d'un glouton           
        else:
            row = [time.ctime(), time.time()]+data  
        ##ecriture           
        with open(path2, 'a') as f:
                w = csv.writer(f)
                w.writerow(row)     
    @staticmethod
    def get_logger(name, col=False):
        ##creation du path
        if col==False:
            path = "./result/solution_log_detailles/"
        else:
            path = "./result/solution_log_colonnes/"
        path1 = path +constantes.LISTE_INSTANCE[constantes.NUM_INSTANCE]+"/"
        if not os.path.exists(path1):
            os.makedirs(path1)
        path2 = path1+constantes.header_time+constantes.LISTE_INSTANCE[constantes.NUM_INSTANCE]+'_'+constantes.strat+'.log'
    
        logger = logging.getLogger(name)
        if constantes.no_logging == True:
            logger.setLevel(logging.CRITICAL)
        else:
            logger.setLevel(logging.INFO)
        # create a file handler
        handler = logging.FileHandler(path2)
        handler.setLevel(logging.INFO)
        # create a logging format
        if col==False:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        #logger.addHandler(handler)
        logger.handlers=[handler]
        return logger
        