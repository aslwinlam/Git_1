
class Cannonball:
    def __init__(self, force, light, angle):  #constructor
            self.force = force  # object variables
            self.light = light
            self.angle = angle
        
    def getvolcity(self):
        x= self.time*self.speed*self.force # number
        return x
    
    def getMath(self):
        x= self.force*self.light*self.speed
        return x
    
    def getMathAdd(self, wind):
         x= self.force*wind
         return x

    def getTime():
        print(Cannonball.time)
        
    time=11  # class variable
    speed=13 # class variable
    lastname="Jay Lam"





## HOW TO USE CLASS AND OBJECT

newyork='NY'

def rename():
    print (newyork)
    global newyork
    newyork="XX'

print newyork


    
cannonObject = Cannonball(1.1,2,4)
y = cannonObject.getvolcity()
z = cannonObject.getMath()
x = cannonObject.getMathAdd(10)

print("cannonObject getvolcity function call " + str(y) )
print(y + 30)
print("cannonObject getMath function call " + str(z))
print("cannonObject getMathAdd function call " + str(x))
print("Class function Cannonball.getTime()")
Cannonball.getTime()

cannonObject2 = Cannonball(3,3,3)
y1 = cannonObject2.getvolcity()
z1 = cannonObject2.getMath()
x1 = cannonObject2.getMathAdd(10)

print(chr(86))


 
print("cannonObject2 getvolcity function call " + str(y1))
print("cannonObject2 getMath function call " + str(z1))
print("cannonObject2 getMathAdd function call " + str(x1))

