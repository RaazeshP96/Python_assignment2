'''
    Imagine you are creating a Super Mario game. You need to define a
    class to represent Mario. What would it look like? If you aren't familiar with
    SuperMario, use your own favorite video or board game to model a player.

'''


class Mario:
    def __init__(self):
        self.level = 0
        self.score = 0

    def start(self):
        print("Start game")

    def jump(self):
        self.score += 1
        print('Mario jump over huddles')

    def gamePoint(self):
        if self.score == 100:
            self.level += 1
            self.score = 100
        return self.score

    def endGame(self):
        print("Game has ended")


player1 = Mario()
player1.start()
player1.endGame()
