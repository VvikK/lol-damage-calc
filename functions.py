from classes import *

#damage of one ability
def ability_damage(champ1, champ2, ability):
    damage = 0
    damage_m = champ1.abilities[ability].magic_damage + (ability.ap_scaling * champ1.base_stats.ap) 
    damage_p = champ1.abilities[ability].physical_damage + (ability.ad_scaling * champ1.base_stats.ad)
    damage_t = ability.true_damage

    armor = champ2.base_stats.armor*(1-champ1.base_stats.armor_pen) - champ1.base_stats.armor_pen_flat
    mr = champ2.base_stats.mr*(1-champ1.base_stats.mr_pen) - champ1.base_stats.mr_pen_flat

    damage = damage_m*(100/(100+armor)) + damage_p*(100/(100+mr)) + damage_t
    return damage

def auto_damage(champ1, champ2):
    armor = champ2.base_stats.armor*(1-champ1.base_stats.armor_pen) - champ1.base_stats.armor_pen_flat
    damage = champ1.ad * (100/(100+armor))
    return damage


