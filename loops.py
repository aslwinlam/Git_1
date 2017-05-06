def whileLoop1():
    count = 0
    while (count<9):
        print ('The count is : ', count)
        print('The count is : ' + str(count))
        count = count +1
    
    print('--------------------')
    lastname="Jay lam"
    counter =0
    while (counter<len(lastname)):
        print('each character of Jay',lastname[counter])
        counter  +=1
    print('--------------------')  

    lastname="Jay lam"
    counter =0
    while (counter<len(lastname)):
        if lastname[counter] ==" ":
            break
        print('each character of Jay',lastname[counter])
        counter  +=1
    print('--------------------')
     
   
    

    for a in 'Python':     # First Example
       print ('Current Letter :', a)
    print('--------------------')
    
    fruits = ['banana', 'apple',  'mango']
    for fruit in fruits:        # Second Example
       print ('Current fruit :', fruit)





whileLoop1()
