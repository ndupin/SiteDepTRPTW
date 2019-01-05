#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:31:32 2017

@author: remimolette
"""
from __future__ import division
###############################################################################
##############################importation module###############################
import imp
from tic import tic
from job import job
import time

class constantes:
    ##LISTE_INSTANCE
    LISTE_INSTANCE=[
"gotic_3_1_10_ex1", "gotic_3_1_10_ex2", "gotic_3_1_10_ex3", "gotic_3_1_10_ex4",
"gotic_3_5_10_ex1", "gotic_3_5_10_ex2", "gotic_3_5_10_ex3", "gotic_3_5_10_ex4",
"gotic_4_1_20_ex4", "gotic_4_2_20_ex4", "gotic_4_3_20_ex4", "gotic_4_5_20_ex4",
"gotic_5_1_20_ex1", "gotic_5_1_20_ex2", "gotic_5_1_20_ex3", "gotic_5_1_20_ex4",
"gotic_5_3_20_ex1", "gotic_5_3_20_ex2", "gotic_5_3_20_ex3", "gotic_5_3_20_ex4",
"gotic_5_5_20_ex1", "gotic_5_5_20_ex2", "gotic_5_5_20_ex3", "gotic_5_5_20_ex4",
"gotic_8_1_20_ex1", "gotic_8_1_20_ex2", "gotic_8_1_20_ex3", "gotic_8_1_20_ex4", "gotic_8_1_20_ex5", 
"gotic_8_3_20_ex1", "gotic_8_3_20_ex2", "gotic_8_3_20_ex3", "gotic_8_3_20_ex4", "gotic_8_3_20_ex5",
"gotic_8_5_20_ex1", "gotic_8_5_20_ex2", "gotic_8_5_20_ex3", "gotic_8_5_20_ex4", "gotic_8_5_20_ex5", 
"gotic_10_1_40_ex1", "gotic_10_1_40_ex2", "gotic_10_1_40_ex3", "gotic_10_1_40_ex4", 
"gotic_10_3_40_ex1", "gotic_10_3_40_ex2", "gotic_10_3_40_ex3", "gotic_10_3_40_ex4", 
"gotic_10_5_40_ex1", "gotic_10_5_40_ex2", "gotic_10_5_40_ex3", "gotic_10_5_40_ex4", 
"gotic_10_10_40_ex1", "gotic_10_10_40_ex2", "gotic_10_10_40_ex3", "gotic_10_10_40_ex4", 
"gotic_15_1_40_ex1", "gotic_15_1_40_ex2", "gotic_15_1_40_ex3", "gotic_15_1_40_ex4", 
"gotic_15_1_40_ex5", "gotic_15_1_40_ex6", "gotic_15_1_40_ex7", "gotic_15_1_40_ex8", 
"gotic_15_3_40_ex1", "gotic_15_3_40_ex2", "gotic_15_3_40_ex3","gotic_15_3_40_ex4", 
"gotic_15_3_40_ex5", "gotic_15_3_40_ex6", "gotic_15_3_40_ex7", "gotic_15_3_40_ex8",
"gotic_15_5_40_ex1", "gotic_15_5_40_ex2", "gotic_15_5_40_ex3", "gotic_15_5_40_ex4",
"gotic_15_5_40_ex5", "gotic_15_5_40_ex6", "gotic_15_5_40_ex7", "gotic_15_5_40_ex8",
"gotic_15_10_40_ex1", "gotic_15_10_40_ex2", "gotic_15_10_40_ex3", "gotic_15_10_40_ex4",
"gotic_15_10_40_ex5", "gotic_15_10_40_ex6", "gotic_15_10_40_ex7", "gotic_15_10_40_ex8",
"gotic_15_20_40_ex1", "gotic_15_20_40_ex2", "gotic_15_20_40_ex3", "gotic_15_20_40_ex4",
"gotic_15_20_40_ex5", "gotic_15_20_40_ex6", "gotic_15_20_40_ex7", "gotic_15_20_40_ex8",
"gotic_10_3_50_ex1", "gotic_10_3_50_ex3", "gotic_10_3_50_ex4", "gotic_10_3_50_ex5", "gotic_10_3_50_ex6", 
"gotic_15_3_50_ex1", "gotic_15_3_50_ex3", "gotic_15_3_50_ex4", "gotic_15_3_50_ex5",
 "gotic_15_3_50_ex6", "gotic_15_3_50_ex14", "gotic_15_3_50_ex15", "gotic_15_3_50_ex16", 
"gotic_15_3_80_ex1", "gotic_15_3_80_ex2", "gotic_15_3_80_ex4", "gotic_15_3_80_ex5", 
"gotic_20_3_50_ex1", "gotic_20_3_50_ex2", "gotic_20_3_50_ex4", "gotic_20_3_50_ex5", "gotic_20_3_50_ex6",
"gotic_20_3_80_ex1", "gotic_20_3_80_ex2", "gotic_20_3_80_ex4", "gotic_20_3_80_ex5",
"gotic_20_3_100_ex1", "gotic_20_3_100_ex3", "gotic_20_3_100_ex4", "gotic_20_3_100_ex5"
]  
    
    ########################################CONSTANTES PATH####################
    #PATH_INSTANCE = "./data/"
    PATH_INSTANCE = "./instances/"
    PATH_RESULT = "./result/"
    ################################CONSTANTES LOCALSOLVER ####################
    LS_TIME_LIMIT=15
    ################################PARAMETRES SIMULATION######################
    ##nombre de tours maximum non utilise pour une colonne
    #TODO: non implenté
    #column_ttl=3
    ##definition de l'entete timestamp du fichier log
    #header_time="non_init"
    ##logging level
    #no_logging = False
    ##startegie de gloutons
    #strat=""
    
    @staticmethod
    def init(NUM_INSTANCE=0):
        constantes.NUM_INSTANCE=NUM_INSTANCE
        ##path ver s les instances
        constantes.INSTANCE=constantes.LISTE_INSTANCE[NUM_INSTANCE]
        #chargement de la classe data correspondant au nom de l'instance
        data = imp.load_source(constantes.INSTANCE, constantes.PATH_INSTANCE+constantes.INSTANCE+".py")
        data_2=data.data
        ##definition de l'entete timestamp du fichier log
        time_temp = time.ctime()
        header_time = (time_temp.split(":")[0]).split(" ")
        try:
            header_time.remove("")
        except:
            pass
        header_time.append(time_temp.split(":")[1])
        header_time2=""
        header_time2 += header_time[0]+"_"+header_time[1]+"_"+header_time[2]+"_"
        header_time2 += header_time[3]+":"+header_time[4]+"_"
        constantes.header_time = header_time2
        ###############################################################################
        #########################definition constantes de l'instance###################
        ##extraction des constantes
        constantes.nbJOB=data_2["nbJOB"]
        constantes.tics=data_2["tics"]
        constantes.nbTIC=data_2["nbTIC"]
        constantes.speed=data_2["speed"]
        constantes.nbCMP=data_2["nbCMP"]
        constantes.name=data_2["name"]
        constantes.jobs=data_2["jobs"]
        
        ###############################################################################
        #########################initialisation des listes d'objet#####################
        ##liste de techniciens
        #print('*** creation liste des tics')
        constantes.TICS=[tic(t) for t in constantes.tics]
        #for t in TICS: print(t)
        
        ##liste des jobs
        #print('*** creation liste des jobs')
        constantes.JOBS=[job(j) for j in constantes.jobs]
        #for j in JOBS: print(j)
        
        ##dico tic pour acces rapide
        constantes.dico_tic={}
        for t in constantes.TICS:
            constantes.dico_tic[t.id]=t
        tic.dico_tic=constantes.dico_tic
    
        ##dico job pour acces rapide
        constantes.dico_job={}
        for j in constantes.JOBS:
            constantes.dico_job[j.id]=j
        job.dico_job=constantes.dico_job    
        
        #job.speed
        job.speed=constantes.speed
        
        ###############################################################################
        ##########################constantes calculées#################################
        ##distance entre deux jobs
        constantes.distance={}
        for job1 in constantes.JOBS:
            for job2 in constantes.JOBS:
                constantes.distance[(job1.id,job2.id)]=job.distance(job1,job2)
    
        ##duree entre deux jobs pour faire le trajet
        constantes.temps={}
        for job1 in constantes.JOBS:
            for job2 in constantes.JOBS:
                constantes.temps[(job1.id,job2.id)]=job.temps(job1,job2)
    
'''         
        ##duree minimale entre le debut d'un job et le debut de la suivante
        constantes.intervalle_min={}
        for job1 in constantes.JOBS:
            for job2 in constantes.JOBS:
                temp=job.temps(job1,job2)+job1.dur
                constantes.intervalle_min[(job1.id,job2.id)]=temp
                              
        ###                       
        constantes.rarete_job = {}
        for j in constantes.JOBS:
            constantes.rarete_job[j.id]=0
            for t in constantes.TICS:
                if(j.cmp in t.cmp_list):
                    constantes.rarete_job[j.id] +=1
            constantes.rarete_job[j.id] = 1-(constantes.rarete_job[j.id]/len(constantes.JOBS))   
        job.rarete_job = constantes.rarete_job
        ###
        constantes.rarete_job_2 = {}
        for j in constantes.JOBS:
            constantes.rarete_job_2[j.id]=0
            for t in constantes.TICS:
                t_deb=max(t.t_start+job.temps(t,j),j.t_min)
                t_fin=t_deb+j.dur
                if(j.cmp in t.cmp_list)and(t_deb<=j.t_max)and(t_fin<=t.t_end-job.temps(j,t)):
                    constantes.rarete_job_2[j.id] +=1
            constantes.rarete_job_2[j.id] = 1-(constantes.rarete_job_2[j.id]/len(constantes.JOBS))   
        job.rarete_job_2 = constantes.rarete_job_2  
    
        ###
        constantes.rarete_job_3 = {}
        for j in constantes.JOBS:
            constantes.rarete_job_3[j.id]=0
            for t in constantes.TICS:
                t_deb=max(t.t_start+job.temps(t,j),j.t_min)
                t_fin=t_deb+j.dur
                if(j.cmp in t.cmp_list)and(t_deb<=j.t_max)and(t_fin<=t.t_end-job.temps(j,t)):
                    constantes.rarete_job_3[j.id] +=1*(j.t_max-j.t_min)/(t.t_end-t.t_start)
            constantes.rarete_job_3[j.id] = 1-(constantes.rarete_job_3[j.id]/len(constantes.JOBS))   
        job.rarete_job_3 = constantes.rarete_job_3        
'''            
