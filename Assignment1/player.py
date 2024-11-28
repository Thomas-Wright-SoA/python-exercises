class Player:
    name = ""
    balance = 0
    lvl = 1
    xp = 0
    
    def __init__(self, name):
        self.name = name
        print(f"Welcome {name}, let's play!")
        print(self.stats())

    # returns at what XP the next level up should occur
    def next_lvl_up(self):
        return self.lvl * self.lvl

    def add_xp(self, newxp):
        self.xp += newxp
        print(f"+{newxp}xp")
        if self.xp >= self.next_lvl_up():
            self.lvl += 1
            print("You leveled up!")
        return
    
    def stats(self):
        return f"[ Name: {self.name} | Balance: £{self.balance:.2f} | Level: {self.lvl} | XP: {self.xp} | Next LVL: +{(self.next_lvl_up()) - self.xp}xp ]"