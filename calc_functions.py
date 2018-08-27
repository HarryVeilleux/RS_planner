# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:23:19 2018

@author: VeiHa001
"""

import math
import csv
import numpy as np
import pandas as pd

def plan_lvl(skill, target, current=None, exp = False, showall = False) :
    """ Generalized planner """
    if current is None :
        curr_exp = user_dict[skill]
        current = max(exp_df['level'][exp_df['exp']<=curr_exp])
        print('Defaulting to: Level ' 
              + str(current) + ', ' + str(curr_exp) + ' experience\n')
    elif exp == True :
        curr_exp = current
        current = max(exp_df['level'][exp_df['exp']<=curr_exp])
        print('Current level: ' + str(current))
    else :
        curr_exp = exp_df.loc[current-1,'exp'] # Returns exp total given level
    
    targ_exp = exp_df.loc[target-1,'exp']
    exp_diff = targ_exp - curr_exp
    
    skill_df = actions_df[actions_df['skill']==skill] # Subset full skill df for skill
    rel_df = skill_df[np.logical_or(np.logical_and(skill_df['level']<target,
                                                   skill_df['always']==True), # always = True rows are included but later logic does not show them
                                    np.logical_and(skill_df['level']>=max(skill_df[skill_df['level']<=current]['level']),
                                                   skill_df['level']<target))] # Subset for only relevant methods
       
    exp_dict = {} # Dictionary of actions from curr to targ OR breakpoint to targ
    bp_dict = {} # Dictionary of breakpoint methods/levels
    first_act = ''
    for i, row in rel_df.iterrows() :
        if row['level'] == min(rel_df['level']) :
            round_val = math.ceil(exp_diff/row['exp'])
            exp_dict[row['method']] = round_val # Add first method(s)
            if first_act == '' :
                first_act = [row['method'], str(round_val), row['exp']] # Store first method name, no. of actions, and exp
            else :
                bp_dict[row['method']] = row['level']
        else :
            round_val = math.ceil((targ_exp-exp_df['exp'][exp_df['level']==row['level']])/row['exp'])
            exp_dict[row['method']] = round_val # Add actions from breakpoint to target
            bp_dict[row['method']] = row['level']

    counter = 1
    print(str(counter) + '. ' + first_act[1] + ' ' + first_act[0]) # Print first method
    for i, j in bp_dict.items() : # Print each other path
        counter = counter + 1
        first_act_val = math.ceil((exp_df.loc[j,'exp']-curr_exp)/first_act[2])

        if first_act_val<=0 :
            print(str(counter) + '. ' + str(exp_dict[i]) + ' ' + i)
        else :
                print(str(counter) + '. ' + str(first_act_val) + ' ' + first_act[0] + ' then ' + str(exp_dict[i]) + ' ' + i)

def update_user(exp=False,**skills):
    """ Update user dictionary with new experience """
    print('BEFORE')
    for k, v in user_dict.items() : # Print previous level/experience values
        if k in skills.keys() :
            old_lvl = max(exp_df['level'][exp_df['exp']<=v])
            print(k.capitalize() + ': Level ' + str(old_lvl) + ', ' + str(v) + ' experience')
        
    print('\nAFTER')
    
    if exp == True : # Update user_dict with new experience values
        for k, v in skills.items() :
            user_dict[k] = v
    else :
        for k, v in skills.items() :
            user_dict[k] = int(exp_df.loc[v-1,'exp'])
            
    for k, v in user_dict.items(): # Print new level/experience values
        if k in skills.keys() :
            new_lvl = max(exp_df['level'][exp_df['exp']<=v])
            print(k.capitalize() + ': Level ' + str(new_lvl) + ', ' + str(v) + ' experience')

#
#
#
#
         
""" Old code """

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