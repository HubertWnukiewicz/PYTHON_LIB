
def printFileName():
    print("Person")

class Person:
    status=None

    def __init__(self,status):
        self.status=status

    def getStatus(self):
        return self.status

    def setStatus(self,status):
        self.status=status

    def printStatus(self):
        print("{}".format(self.status))