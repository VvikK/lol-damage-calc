class Champ:
    def __init__(self, name, base_stats, abilities):
        self.name = name
        self.base_stats = base_stats
        self.abilities = abilities
        

class base_stats:
    def __init__(self, hp, mp, ad, ap, armor, mr, aspd, ms):
        self.hp = hp
        self.mp = mp
        self.ad = ad
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.aspd = aspd
        self.ms = ms

        self.apen = 0
        self.flat_apen = 0
        self.mpen = 0
        self.flat_mpen = 0

class ability:
    def __init__(self, name, magic_damage, physical_damage, true_damage, effects):
        self.name = name
        self.magic_damage = 0
        self.ap_scaling = 0
        self.physical_damage = 0
        self.ad_scaling = 0
        self.true_damage = 0
        self.effects = []

