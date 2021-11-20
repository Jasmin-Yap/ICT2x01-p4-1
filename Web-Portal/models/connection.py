class Connection:
    def __init__(self, ip="", port=""):
        self.__ip = ""
        self.__port = ""

    def get_ip(self):
        return self.__ip

    def get_port(self):
        return self.__port

    def set_ip(self, ip):
        self.__ip = ip

    def set_port(self, port):
        self.__port = port
