from quest_guide import *
from rs_character import *

username = 'big jammer p' # input("RS name: ")
user = Character(username)

my_quest = input("What quest do you want to complete? ")

curr_quest = Quest(my_quest)
curr_guide = Guide(curr_quest, user)
curr_guide.run_guide()

# skill_dict = user.update()
# for k, v in skill_dict.items():
#     print(k+ ': ' + str(v))
# skill = input("Skill: ")
# print(user.level(skill))
