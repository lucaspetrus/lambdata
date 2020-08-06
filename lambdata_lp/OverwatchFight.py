#classes always use upper case
class OverwatchCharacters:
    """This class is used to take in Overwatch Characters attributes in order to help assemble the correct team"""
    def __init__(self, playerclass, health, speed, damage, healing, shield, winrate):
        self.playerclass = playerclass
        self.health = health
        self.speed = speed
        self.damage = damage
        self.healing = healing
        self.shield = shield
        self.winrate = winrate


    def __str__(self):
        return f"{self.playerclass} {self.health}"


class Healer(OverwatchCharacters):
    """This class looks deeper into the Healers attributes"""

    def __init__(self, playerclass, health, speed, damage, healing, shield, winrate,
                 heals10min, selfheals, ultheals, secondaryheal):
        super().__init__(playerclass, health, speed, damage, healing, shield, winrate)
        self.secondaryheal = secondaryheal
        self.ultheals = ultheals
        self.selfheals = selfheals
        self.heals10min = heals10min


class Attacker(OverwatchCharacters):
    """This class looks deeper into Attacker attributes"""
    def __init__(self, playerclass, health, speed, damage, healing, shield, winrate,
                 damage10min, damageult, deathspergame):
        super().__init__(playerclass, health, speed, damage, healing, shield, winrate)
        self.damage10min = damage10min
        self.damageult = damageult
        self.deathspergame = deathspergame


class Tanks(OverwatchCharacters):
    """This class looks at differences in DPS playerclass"""
    def __init__(self, playerclass, health, speed, damage, healing, shield, winrate,
                 damage10min, damageblocked, killsperlife):
        super().__init__(playerclass, health, speed, damage, healing, shield, winrate)
        self.damage10min = damage10min
        self.damageblocked = damageblocked
        self.killsperlife = killsperlife


if __name__ == '__main__':
    """Below is a list of all Overwatch Character individual statistics from competitive season 20"""
    #playerclass, health, speed, damage, healing, shield, winrate)
    Ana = Healer('Ana', 200, 3, 2264, 6713, 0, .47, 400, 600, 0, 8600)
    Lucio = Healer('Lucio', 145, 60, 50, 20, 375, 115)
    print(Ana)