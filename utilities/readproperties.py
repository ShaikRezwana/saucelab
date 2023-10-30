import configparser

config=configparser.RawConfigParser()
config.read(r"C:\\Users\\rezwana.shaik\\PycharmProjects\\sauce.py\\configurations\\config.ini")

class Readconfig:

    @staticmethod
    def getbaseurl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def enterusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def enterpassword():
        password=config.get('common info', 'password')
        return password