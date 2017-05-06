def loopTen():
    x=1   
    y=3
    for index in range(10):
        x=x+1
        y=y+1
        if x == 12:
            print("break")
            break
        print("Outside loop " + str(index) +"...x=" +str(x))
        for w in range(3):
            x=x+1
            print("  inside loop w=" +str(w)+"  x="+ str(x))
    print ('end')
    print (x)
    print (y)
