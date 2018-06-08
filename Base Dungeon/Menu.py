from player_data import *

class Menu:
    def __init__(self, hero_stats, skills, inventory):
        self.hero_stats = hero_stats
        self.skills = skills
        self.inventory = inventory

class Hero_Stats_Menu:
    def __init__(self, name, lvl, HP, MP, current_exp, exp_next):
        self.name = name
        self.lvl = lvl
        self.HP = HP
        self.MP = MP
        self.current_exp = current_exp
        self.exp_next = exp_next

class Skill_Book_Menu:
    def __init__(self, sword, fire, water):
        self.sword = sword
        self.fire = fire
        self. water = water
        #self.skill_owned = skill_owned
        #self.skill_unowned = skill_unowned

