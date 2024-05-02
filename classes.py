class Champ:
    def __init__(self, name, level, base_stats, abilities):
        self.name = name
        self.level = level
        self.base_stats = base_stats
        self.abilities = abilities
        

class base_stats:
    def __init__(self, hp, mpen, ad, ap, armor, mr, aspd, aspd_growth, ms, apen, flat_apen, flat_mpen):
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
    def __init__(self, name, magic_damage, physical_damage, true_damage, effects):
        self.name = name
        self.magic_damage = 0
        self.ap_scaling = 0
        self.physical_damage = 0
        self.ad_scaling = 0
        self.true_damage = 0
        self.effects = []

