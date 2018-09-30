""" Quest guide for OSRS """

class Guide(object):

    def __init__(self, quest_name, character):
        self.quest_name = quest_name
        self.character = character

    def run_guide(self):
        reqs, steps, more = self.quest_name.read_quest()
        skills, quests = self.character.update()
        curr = 1
        missing = []

        for quest in reqs['quest']:
            if quest in quests:
                next
            else:
                missing.append(quest.capitalize())

        skill_reqs = reqs['skill']

        for skill, level in skill_reqs.items():

            if level > self.character.level(skill):
                missing.append(skill.capitalize() + ' level ' + str(level))
            else:
                next

        if len(missing) > 0:
            print("Missing requirements: ", end = '')
            for require in missing[:-1]:
                print(require + ', ', end = '')
            print(missing[-1])

            cont = input("Continue anyway?\n> ")

            if cont.lower() in ['y', '']:
                pass
            else:
                exit(1)

        else:
            print("All requirements met!")

        item_reqs = reqs['item']

        print("Required items:")
        for item, qty in item_reqs.items():
            print(item.capitalize() + ' x' + str(qty))

        command = input("Press c to enter checklist. Any other key to continue. ")

        if command.lower() == 'c':
            self.quest_name.checklist(item_reqs)
        else:
            pass

        while curr < len(steps) - 1:
            if str(curr) in more.keys():
                print('*', end = '')

            print(str(curr) + '. ' + steps[curr])
            command = input("> ")

            if command in ['n', 'next', '']:
                curr += 1
            elif command in ['b', 'back']:
                if curr == 1:
                    print("Guide is already at step 1.")
                else:
                    curr -= 1
            elif command in ['m', 'more']:
                try:
                    print(more[str(curr)])
                except KeyError:
                    print("No additional information available.")
            else:
                print("Command not available")

        print("Quest complete!")


class Quest(object):

    quests = {
        "doric's quest": "doricsquest.txt",
        "cook's assistant": "cooksassistant.txt",
        "nature spirit": "naturespirit.txt",
        "lunar diplomacy": "lunardiplomacy.txt",
        "my arm's big adventure": "myarmsbigadventure.txt",
        "making friends with my arm": "makingfriendswithmyarm.txt"
    }

    def __init__(self, quest_name):
        self.quest_name = quest_name.lower()

    def read_quest(self):
        file_name = Quest.quests.get(self.quest_name)
        steps = []
        reqs = {}
        more = {}

        with open(file_name) as file:
            m_count = 3
            for num, line in enumerate(file):
                if num == 0:
                    if line.strip() == "none":
                        next
                    else:
                        skill_list = line.split(';')
                        skill_reqs = {}
                        for skill in skill_list:
                            skill_reqs[skill.split(',')[0]] = int(skill.split(',')[1])
                            reqs['skill'] = skill_reqs

                elif num == 1:
                    if line.strip() == "none":
                        next
                    else:
                        quest_list = [quest.strip() for quest in line.split(',')]
                        reqs['quest'] = quest_list

                elif num == 2:
                    if line.strip() == "none":
                        next
                    else:
                        item_list = line.split(';')
                        item_reqs = {}
                        for item in item_list:
                            item_reqs[item.split(',')[0]] = int(item.split(',')[1])
                            reqs['item'] = item_reqs

                elif line.startswith('[m]'):
                    more[str(num - m_count)] = line.strip()
                    m_count += 1

                else:
                    steps.append(line.strip())

        return reqs, steps, more

    def checklist(self, item_dict, have = []):

        def display(item_dict, have):
            for item, qty in item_dict.items():
                if item in have:
                    print('[X] ', end = '')
                else:
                    print('[ ] ', end = '')

                print(item.capitalize() + ' x' + str(qty))

        for item, qty in item_dict.items():
            if item in have:
                pass
            else:
                print(item.capitalize() + ' x' + str(qty))
                user_have = input("Have item? (Y/N) ")

                if user_have.lower() == 'y':
                    have.append(item)

                elif user_have.lower() in ['display', 'd', 'full', 'f', 'list', 'l']:
                    display(item_dict, have)

                elif user_have.lower() in ['exit', 'e', 'continue', 'cont']:
                    return

                else:
                    pass

        display(item_dict, have)

        if len(have) == len(item_dict.keys()):
            print("All items acquired!")
            return
        else:
            command = input("Run again? ")

            if command.lower() == 'y':
                return self.checklist(item_dict, have)
            else:
                return
