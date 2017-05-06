newyork='NY'

def rename():
  
    global newyork
    print(newyork)
    newyork="XX"
    print(newyork)


print('before print ' + newyork)
rename()
print('last print ' + newyork)
