from typing import Any


class Champ:
    def __init__(self, name, level, base_stats, abilities):
        self.name = name
        self.level = level
        self.base_stats = base_stats
        self.abilities = abilities
        

class base_stats:
    def __init__(self, hp, mpen, ad, ap, armor, mr, aspd, aspd_growth, ms, apen, flat_apen, flat_mpen):
        #All champion base stats
        self.hp = hp
        self.mpen = mpen
        self.ad = ad
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.aspd = aspd
        self.aspd_growth = aspd_growth
        self.ms = ms
        self.apen = apen
        self.flat_apen = flat_apen
        self.flat_mpen = flat_mpen


class ability:
    def __init__(self, name, magic_damage, physical_damage, ap_scaling, ad_scaling, true_damage, effects, statChange, statChangeEnemy):
        #Ability Information
        self.name = name
        self.magic_damage = magic_damage
        self.ap_scaling = ap_scaling
        self.physical_damage = physical_damage
        self.ad_scaling = ad_scaling
        self.true_damage = true_damage
        self.effects = []
        #Change to base stats, i.e. statChange = [0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0]
        self.statChange = statChange
        self.statChangeEnemy = statChangeEnemy
    
        


