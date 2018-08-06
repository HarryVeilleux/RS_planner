# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:23:19 2018

@author: VeiHa001
"""

import math

#def furn_to_target(target, current = 1, exp = False) :
#    """ Given target level and optional current level, give furniture options """
#    if exp == False :
#        curr_exp = exp_table[current]
#    else :
#        curr_exp = current
#    
#    target_mats = mats_to_lvl(exp_table[target]-curr_exp)
#    print(target_mats)  
#    
#    for i, j in train_furn.items() :
#        furn = math.ceil(target_mats[j['material']]/j['number'])
#        print(i+': '+str(furn))
        
def acts_to_lvl(skill, target, current = 1, exp = False) :
    """ Generalized skill calculator """
    if exp == False :
        curr_exp = exp_table[current]
    else :
        curr_exp = current
    
    exp_dict = {}
    for i, j in actions[skill].items() :
        round_val = math.ceil((exp_table[target]-curr_exp)/j)
        exp_dict[i] = round_val
    return exp_dict