class Token:
    def __init__(self, token = None,  studentName = None):
        self.__token = token

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token
    
    def set_studentName(self, studentName):
        self.__studentName = studentName
    
    def get_studentName(self):
        return self.__studentName