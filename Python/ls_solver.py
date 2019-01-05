#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:18:11 2017

@author: remimolette
"""
from __future__ import division
import localsolver
import copy
from constantes import constantes
from job import job
#from solution import solution


class ls_prob():
    
    def __init__(self):
        self.prob=None
        self.TICS=[]
        self.JOBS=[]
        self.u_index=[]
        self.U = {}
        self.T = {}
    @classmethod
    def ls_problem(self, liste_tic=False,liste_job=False,instance=0,no_pen=False,affectation={},dual = -1, time_limit=10):
###############################################################################
###################    initialisation variables   #############################
###############################################################################
        res=ls_prob()
        if(liste_tic==False):
            TICS=copy.deepcopy(constantes.TICS)
##restriction du problème à un sous ensemble de tic        
        else:
            TICS=copy.deepcopy(constantes.TICS)
            TICS=[t for t in TICS if t.id in liste_tic]

        if(liste_job==False):
            JOBS=copy.deepcopy(constantes.JOBS)
##restriction du problème à un sous ensemble de tic et de job            
        else:
            JOBS=copy.deepcopy(constantes.JOBS)
            JOBS=[j for j in JOBS if j.id in liste_job]     

        res.JOBS=JOBS
        res.TICS=TICS
        ind_jobs=[j.id for j in JOBS]
        ind_jobs.insert(0,0)
        ind_tics=[t.id for t in TICS]
        ind_tics_2=[t.id for t in TICS]
        ind_tics_2.insert(0,0)

        ####creation des données initiales pourlocalsolver
        nb_job=len(res.JOBS)
        nb_tic=len(res.TICS)
        t_min=[j.t_min for j in res.JOBS]
        t_max=[j.t_max for j in res.JOBS]
        t_start=[t.t_start for t in res.TICS]
        t_end=[t.t_end for t in res.TICS]
        dur=[j.dur for j in res.JOBS]

###############################################################################
########################    localsolver   #####################################
###############################################################################
        with localsolver.LocalSolver() as ls:
            #
            # Declares the optimization model
            #
            model = ls.model
    
            # Sequence of customers visited by each truck.
            jobs_sequences = [model.list(nb_job) for k in range(nb_tic)]
            ##ajout des contraintes de compétences
            #localsolver.LSOperator.INDEXOF(jobs_sequences[1],1)==-1            
            # All customers must be visited by  the trucks
            ##TODO creer technicien fictif
            for k in range(nb_tic):
                cmp_list=TICS[k].cmp_list
                #cmp_list=[t for t in TICS if t.id==k+1][0].cmp_list
                for j in range (nb_job):
                    comp=JOBS[j].cmp
                    #comp=[jj for jj in JOBS if jj.id==j+1][0].cmp
                    if comp not in cmp_list: 
                        model.constraint(model.index(jobs_sequences[k],j)==-1)
            model.constraint(model.partition(jobs_sequences))
            
            # Create demands, earliest, latest and service as arrays to be able to access it with an "at" operator
            t_min_array = model.array(t_min)
            t_max_array = model.array(t_max)
            t_start_array = model.array(t_start)
            t_end_array = model.array(t_end)
            dur_array=model.array(dur)
            # Create distance as an array to be able to acces it with an "at" operator
            distance_array = model.array()
            temps_array = model.array()
            for j1 in res.JOBS:
                distance_matrix=[]
                temps_matrix=[]
                for j2 in res.JOBS:
                    distance_matrix.append(job.distance(j1,j2))
                    temps_matrix.append(job.temps(j1,j2))
                distance_array.add_operand(model.array(distance_matrix))
                temps_array.add_operand(model.array(temps_matrix))
            
            distance_warehouse_array = model.array()
            temps_warehouse_array = model.array()
            for t in res.TICS:
                distance_warehouse_matrix=[]
                temps_warehouse_matrix=[]
                for j1 in res.JOBS:
                    distance_warehouse_matrix.append(job.distance(t,j1))
                    temps_warehouse_matrix.append(job.temps(t,j1))              
                distance_warehouse_array.add_operand(model.array(distance_warehouse_matrix))
                temps_warehouse_array.add_operand(model.array(temps_warehouse_matrix))
    
            route_distances = [None for n in res.TICS]
            end_time = [None for n in res.TICS]
            test_temp = [None for n in res.TICS]
            home_lateness = [None for n in res.TICS]
            lateness = [None for n in res.TICS]
    
            # A truck is used if it visits at least one customer
            trucks_used = [(model.count(jobs_sequences[k]) > 0) for k in range(nb_tic)]
            #nb_trucks_used = model.sum(trucks_used)
    
            for k in range(nb_tic):
                sequence = jobs_sequences[k]
                c = model.count(sequence)
                            
                # Distance traveled by each truck
                dist_selector = model.function(lambda i: model.at(distance_array, sequence[i-1], sequence[i]))
                route_distances[k] = model.sum(model.range(1,c), dist_selector) + \
                     model.iif(c > 0, model.at(distance_warehouse_array,k,sequence[0]) + model.at(distance_warehouse_array,k, sequence[c-1]),0)   
                     
                # End of each visit
                ##TODO a modifier pourauthoriser un temps d'attente?
                end_selector = model.function(lambda i, prev: model.max(t_min_array[sequence[i]],
                            model.iif(i == 0,model.at(t_start_array,k)+model.at(temps_warehouse_array,k,sequence[0]), \
                                      prev + model.at(temps_array,sequence[i-1],sequence[i]))) + \
                            model.at(dur_array, sequence[i]))
                end_time[k] = model.array(model.range(0,c), end_selector)
                
                
                #test_temp[k] = end_time[k][0]



                # Arriving home after max_horizon
                home_lateness[k] = model.iif(trucks_used[k], \
                   model.max(0,model.at(end_time[k],c-1) + model.at(temps_warehouse_array,k,sequence[c-1])-t_end[k]), \
                    0)
    
                # completing visit after latest_end
                ##TODO retirer dur du job
                late_selector = model.function(lambda i:  model.max(0,model.at(end_time[k],i)-model.at(dur_array, sequence[i]) - model.at(t_max_array, sequence[i])))
                lateness[k] = home_lateness[k] + model.sum(model.range(0,c),late_selector) 
    
                            
    
            # Total lateness
            total_lateness = model.sum(lateness)
           
    
            # Total distance travelled
            total_distance = model.sum(route_distances);
    
    
            # Objective: minimize the number of trucks used, then minimize the distance travelled
            model.minimize(total_lateness)
            model.minimize(total_distance)
    
            model.close() 
            
            #
            # Parameterizes the solver
            #

            ls.create_phase().time_limit = time_limit
            ls.solve()
            
            #
            # Writes the solution in a file with the following format :
            #  - number of trucks used and total distance
            #  - for each truck the nodes visited (omitting the start/end at the depot)
            #
            #print("%d %d\n" % (total_lateness.value,total_distance.value))
            print(constantes.INSTANCE)
            print(total_distance.value)
            return total_distance.value + 100000 * total_lateness.value


        #return total_distance.value + 100000 * total_lateness.value


