""" Structure of OSRS character """
import csv
import pandas as pd

class Character(object):

    user_csv = {
        'big jammer p': 'bjp_',
        'big jammer k': 'bjk_'
    }

    def __init__(self, username):
        self.username = username.lower()

    def update(self):
        file_name = Character.user_csv.get(self.username)

        if file_name is None:
            print("RS name not recognized")
            exit(1)

        else:
            with open(file_name + 'skill.csv') as file:
                reader = csv.reader(file)
                skills = {rows[0]:int(rows[1]) for rows in reader}

            with open(file_name + 'quest.txt') as file:
                quests = []
                for line in file:
                    quests.append(line.strip())

            return skills, quests

    def level(self, skill):
        exp_df = pd.read_csv('exp.csv')
        user_dict, user_quests = self.update()
        skill_level = max(exp_df['level'][exp_df['exp']<=user_dict[skill.lower()]])

        return skill_level
