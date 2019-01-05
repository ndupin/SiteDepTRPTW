#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:42:05 2017

@author: remimolette
"""
from __future__ import division

class tic:
    dico_tic={}
    def __init__(self,dico):
        self.id=int(dico['id'].split("_")[1])
        self.cmp_list=dico['cmp_list']
        self.t_start=dico['t_start']
        self.t_end=dico['t_end']
        self.x=dico['x']
        self.y=dico['y']
    ##fonction d'affichage
    def __str__(self):
        res=""
        res+='id: '+str(self.id)+"; "
        res+='cmp_list: '+str(self.cmp_list)+"; "
        res+='t_start: '+str(self.t_start)+"; "
        res+='t_end: '+str(self.t_end)+"; "
        res+='x: '+str(self.x)+"; "
        res+='y: '+str(self.y)+"; "
        return res
        
    @staticmethod
    def get(id):
        return tic.dico_tic[id]         
        
        

                
        
        
        
        