# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:11:46 2018

@author: veiha001
"""



def quest_tree(quest, level=0) :
    if quest not in quest_dict.keys() :
        if quest in quest_tags.keys() :
            quest = quest_tags[quest]
        else :
            print('Invalid quest name')
            return
        
    if level==0 :
        print(quest.title() + ':')
        if quest not in quest_dict.keys() :
            print('No quest requirements')
            return
    elif quest not in quest_dict.keys() :
        return
        
    for i in quest_dict[quest] :
        if i in comp_quest :
            box = '[X] '
        else :
            box = '[ ] '
        print(level*'   ' + box + i.title())
        if i in quest_dict.keys() :
            quest_tree(i,level=level+1)

#def update_comp_quest(*quests) :
#    for q in quests :
#        if q not in comp_quest :
#            comp_quest.append(q)
#        update_comp_quest(quest_dict[q])