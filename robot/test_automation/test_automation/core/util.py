import os


class Util:

    def __init__(self): pass

    @staticmethod
    def ping(ip_address):
        response = os.system("ping -c 1 " + ip_address)
        if response == 0:
            return True
        return False

