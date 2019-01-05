#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:57:24 2017

@author: remimolette
"""
from __future__ import division
import numpy as np
#import constantes
class job:
    dico_job={}
    rarete_job={}
    rarete_job_2={}
    rarete_job_3={}
    speed=0
    def __init__(self,dico):
        self.id=int(dico['id'].split("_")[1])
        self.t_max=dico['t_max']
        self.t_min=dico['t_min']
        self.day=dico['day']
        self.dur=dico['dur']
        self.cmp=dico['cmp']
        self.penal=dico['penal']
        self.x=dico['x']
        self.y=dico['y']
    @staticmethod
    def get(id):
        return job.dico_job[id] 

    ##fonction d'affichage
    def __str__(self):
        res=""
        res+='id: '+str(self.id)+"; "
        res+='t_max: '+str(self.t_max)+"; "
        res+='t_min: '+str(self.t_min)+"; "
        res+='day: '+str(self.day)+"; "
        res+='dur: '+str(self.dur)+"; "
        res+='cmp: '+str(self.cmp)+"; "
        res+='penal: '+str(self.penal)+"; "
        res+='x: '+str(self.x)+"; "
        res+='y: '+str(self.y)+"; "
        return res
    
    @staticmethod
    def distance(job1,job2):
        res= int(np.round(np.sqrt((job1.x-job2.x)**2+(job1.y-job2.y)**2)))
        return res
        
    @staticmethod
    def temps(job1,job2):
        res= int(np.round(60.0*job.distance(job1,job2)/job.speed))
        return res

    def rarete(self):
        return job.rarete_job[self.id]

    def rarete_2(self):
        return job.rarete_job_2[self.id]
    def rarete_3(self):
        return job.rarete_job_3[self.id]

    def difficulte(self):
        return 1/(self.t_max-self.t_min)
        
