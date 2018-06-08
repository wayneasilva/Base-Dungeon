class Monster:
    def __init__(self, mob_type, lvl,  name, atk_power, matk_power, HP, MP, exp_value, loot):
        self.mob_type = mob_type
        self.lvl = lvl
        self.name = name
        self.atk_power = atk_power
        self.matk_power = matk_power
        self.HP = HP
        self.MP = MP
        self.exp_value = exp_value
        self.loot = loot