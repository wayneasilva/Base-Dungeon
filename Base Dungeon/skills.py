from player_data import *


class Skill:
    def __init__(self, skill_name, lvl_unlocked, damage_multiplier, mp_cost):
        self.skill_name = skill_name
        self.lvl_unlocked = lvl_unlocked
        self.damage_multiplier = damage_multiplier
        self.mp_cost = mp_cost

    #def check_skill_useable(self):
     #   if player_lvl >= lvl_unlocked:
class use_skill:
    def __init__(self,use_1, use_2, use_3, use_4, use_5):
        self.use_1 = use_1
        self.use_2 = use_2
        self.use_3 = use_3
        self.use_4 = use_4
        self.use_5 = use_5

class Skill_Family:
    def __init__(self, type, skill_1, skill_2, skill_3, skill_4, skill_5):
        self.type = type
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
        self.skill_4 = skill_4
        self.skill_5 = skill_5

##Sword Family Skill Book##

#Skills
sword_slash = Skill('Slash', 3, 1.5, 2)
sword_dblslash = Skill('Double Slash', 7, 3, 3)
sword_run_through = Skill('Run Through', 10, 5, 5)
sword_execute = Skill('Execute', 15, 10, 10)
sword_omnislash = Skill('Omnislash', 20, 100, 1)

#Skill Family
sword = Skill_Family('sword', sword_slash, sword_dblslash, sword_run_through, sword_execute, sword_omnislash)

#Skill Book



