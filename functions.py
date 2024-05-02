from classes import *

def damage(champ1, ability):
    damage = 0
    damage_m = champ1.abilities[ability].magic_damage + (ability.ap_scaling * champ1.base_stats.ap) 
    damage_p = champ1.abilities[ability].physical_damage + (ability.ad_scaling * champ1.base_stats.ad)
    damage_t = ability.true_damage

    #armor = 
    return damage
