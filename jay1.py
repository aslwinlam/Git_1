def loopTen():
    x=1   
    y=3
    for index in range(10,1,1):
        x=x+1
        y=y+1
        print("Outside loop " + str(index))
        print("Outside loop x= " + str(x))
        for w in range(3,1):
            x=x+1
            print("inside loop " + str(x))

    print ('end')
    print (x)
    print (y)
