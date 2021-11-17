class Scoreboard:
    def __init__(self, scoreboard=None):
        self.__scoreboard = scoreboard

    def get_scoreboard(self):
        return self.__scoreboard

    def set_scoreboard(self, scoreboard):
        self.__scoreboard = scoreboard
