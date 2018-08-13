# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:23:19 2018

@author: VeiHa001
"""

import math
import csv
import numpy as np
import pandas as pd

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


def acts_lvl_df(skill, target, current = 1, exp = False, showall = False) :
    """ Generalized skill calculator using pandas DataFrame """
    if exp == False :
        curr_exp = exp_table[current] # Returns exp total given level
    else :
        curr_exp = current
    
    exp_dict = {}
    for i, row in actions_df[actions_df['skill']==skill].iterrows() :
        if showall == False and np.logical_and(row['level'] < current, row['always'] != True) :
            next # Skip underleveled methods
        elif row['level'] <= target :
            round_val = math.ceil((exp_table[target]-curr_exp)/row['exp'])
            exp_dict[row['method']] = round_val # Add relevant methods
        else:
            next # Skip overleveled methods
    return exp_dict

#def plan_lvl(skill, target, current = 1, exp = False, showall = False) :
#    """ Generalized planner """
#    def acts_lvl_df(skill, target, current = 1, exp = False, showall = False) :
#        """ Generalized skill calculator using pandas DataFrame """
#        if exp == False :
#            curr_exp = exp_table[current] # Returns exp total given level
#        else :
#            curr_exp = current
#            
#        exp_dict = {} # Number of actions to level
#        bw_dict = {} # Methods and levels of "between" methods
#        for i, row in actions_df[actions_df['skill']==skill].iterrows() :
#            if showall == False and np.logical_and(row['level'] < current, row['always'] != True) :
#                next # Skip underleveled methods
#            elif np.logical_and(row['level'] <= target, row['level'] > current) :
#                level = row['level']
#                round_val = math.ceil((exp_table[target]-exp_table[level])/row['exp'])
#                exp_dict[row['method']] = round_val # Add methods higher than current but less than target
#                bw_dict[row['method']] = row['level']
#            elif row['level'] <= target :
#                round_val = math.ceil((exp_table[target]-curr_exp)/row['exp'])
#                exp_dict[row['method']] = round_val # Add relevant methods
#            else:
#                next # Skip overleveled methods
#        return exp_dict, bw_dict