# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate(object):
    def __init__(self):
        self.rums = 0

    def drink_rum(self):
        self.rums += 1

    def hows_goin_mate(self):
        if self.rums < 5:
            return('Nothin')
        else:
            return('Arrrr!')

captain = pirate()
captain.drink_rum()
# captain.drink_rum()
# captain.drink_rum()
# captain.drink_rum()
captain.drink_rum()
captain.drink_rum()
print(captain.hows_goin_mate())
