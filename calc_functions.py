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

def plan_lvl(skill, target, current=1, exp = False, showall = False) :
    """ Generalized planner """
    if exp == False :
        curr_exp = exp_table[current] # Returns exp total given level
    else :
        curr_exp = current
    
    targ_exp = exp_table[target]
    exp_diff = targ_exp - curr_exp
    
    skill_df = actions_df[actions_df['skill']==skill] # Subset full skill df for skill
    rel_df = skill_df[np.logical_or(skill_df['always']==True, # always = True rows are included but later logic does not show them
                                    np.logical_and(skill_df['level']>=max(skill_df[skill_df['level']<=current]['level']),
                                     skill_df['level']<target))] # Subset for only relevant methods
    
    exp_dict = {} # Dictionary of actions from curr to targ OR breakpoint to targ
    bp_dict = {} # Dictionary of breakpoint methods/levels
    for i, row in rel_df.iterrows() :
        if row['level'] <= current :
            round_val = math.ceil(exp_diff/row['exp'])
            exp_dict[row['method']] = round_val # Add first method(s)
            first_act = [row['method'], str(round_val), row['exp']] # Store first method name, no. of actions, and exp
        else :
            round_val = math.ceil((targ_exp-exp_table[row['level']])/row['exp'])
            exp_dict[row['method']] = round_val # Add actions from breakpoint to target
            bp_dict[row['method']] = row['level']

    counter = 1
    print(str(counter) + '. ' + first_act[1] + ' ' + first_act[0]) # Print first method
    for i, j in bp_dict.items() : # Print each other path
        counter = counter + 1
        print('OR')
        first_act_val = math.ceil((exp_table[j]-curr_exp)/first_act[2])
        print(str(counter) + '. ' + str(first_act_val) + ' ' + first_act[0] + ' then ' + str(exp_dict[i]) + ' ' + i)