# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:23:19 2018

@author: VeiHa001
"""

import math
import csv

def add_skill(skill, filepath):
    reader = csv.reader(open(filepath, 'r'))
    skill_dict = dict((rows[0],float(rows[1])) for rows in reader)
    actions[skill] = skill_dict
        
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