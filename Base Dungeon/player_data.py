from skills import *

class Player:
    def __init__(self, name, player_lvl, current_exp, lvlup_exp, HP, MP, player_atk, weapon, skills, inventory):
        self.name = name
        self.player_lvl = player_lvl
        self.current_exp = current_exp
        self.lvlup_exp = lvlup_exp
        self.HP = HP
        self.MP = MP
        self.player_atk = player_atk
        self.weapon = weapon
        self.skills = skills
        self.inventory = inventory

    def level_up(self):
        if self.current_exp >= self.lvlup_exp:
            self.player_lvl += 1
            print('Congratulations! You are now level ', self.player_lvl, '!')

            self.lvlup_exp *= 1.5
            print(self.lvlup_exp, ' needed to reach next level')

            self.HP *= .25
            print(self.HP)

            self.MP *= .5
            print(self.MP)


#check when mob killed




