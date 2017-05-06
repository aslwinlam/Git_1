class Cannonball:
    def getVolcity(self):  # object function/method
        x= self.time* self.speed
        return x

    def getBuster():   # class functioin/method
        print(Cannonball.speed*Cannonball.time)

    def __init__(self, time):
        self.time = time
        
    speed=10
    time=39

Cannonball.getBuster()

cannonObject = Cannonball(20)  # this is class created object
y = cannonObject.getVolcity()  # calling the object function
print(y)
