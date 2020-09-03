class Overwatch:
    """This class is used to take in Overwatch Characters attributes in order to help assemble the correct team"""
    def __init__(self, playerclass=10, health=5, speed=6, damage=0, healing=0, shield=0, winrate=0):
        self.playerclass = playerclass
        self.health = health
        self.speed = speed
        self.damage = damage
        self.healing = healing
        self.shield = shield
        self.winrate = winrate

    def __str__(self):
        return f"{self.playerclass} {self.health}"


class Healer(Overwatch):
    """This class looks deeper into the Healers attributes"""

    def __init__(self, playerclass, health, speed, damage, healing, shield, winrate,
                 heals10min, selfheals, ultheals, secondaryheal):
        super().__init__(playerclass, health, speed, damage, healing, shield, winrate)
        self.secondaryheal = secondaryheal
        self.ultheals = ultheals
        self.selfheals = selfheals
        self.heals10min = heals10min