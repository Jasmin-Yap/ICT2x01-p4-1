import pandas as pd
from datetime import datetime


class Scoreboard:
    def __init__(self, data=None, score=[], attempt=[]):
        self.__date = datetime.today().strftime('%d-%m-%Y')
        self.__data = data
        self.__score = score
        self.__attempt = attempt

    def get_date(self):
        return self.__date

    def set_data(self, data):
        self.__data = pd.read_csv(data)

    def get_data(self):
        return self.__data

    def set_attempt(self, attempt):
        for i in range(len(attempt)):
            self.__attempt.append(attempt.iloc[i:i + 1, 0:1])
            print(type(self.__attempt[i]))
            if type(self.__attempt[i]) is not str:
                self.__attempt[i] = self.__attempt[i].to_string(index=False, header=False)

    def get_attempt(self):
        return self.__attempt

    def set_score(self, score):
        for i in range(len(score)):
            self.__score.append(score.iloc[i:i+1, 1:2])
            if type(self.__score[i]) is not str:
                self.__score[i] = self.__score[i].to_string(index=False, header=False)

    def get_score(self):
        return self.__score
