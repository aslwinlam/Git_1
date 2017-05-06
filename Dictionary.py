
class Cannonball:
    def __init__(self, force, light, angle):
            self.force = force
            self.light = light
            self.angle = angle
        
    def getvolcity(self):
        x= self.time*self.speed*self.force
        return x
    
    def getMath(self):
        x= self.force*self.light*self.speed
        return x
    
    def getMathAdd(self, wind):
         x= self.force*wind
         return x

    def getTime():
        print(cannonball.time)
        
    time=11
    speed=13


cannonObject = Cannonball(1,2,4)
y = cannonObject.getvolcity()
z = cannonObject.getMath()
x = cannonObject.getMathAdd(10)

print("cannonObject getvolcity function call " + str(y))
print("cannonObject getMath function call " + str(z))
print("cannonObject getMathAdd function call " + str(x))
print("Class function Cannonball.getTime()")
Cannonball.getTime()

cannonObject2 = Cannonball(3,3,3)
y1 = cannonObject2.getvolcity()
z1 = cannonObject2.getMath()
x1 = cannonObject2.getMathAdd(10)
print("cannonObject2 getvolcity function call " + str(y1))
print("cannonObject2 getMath function call " + str(z1))
print("cannonObject2 getMathAdd function call " + str(x1))

