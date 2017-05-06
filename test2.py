import csv

def test_data(filename, col, day):
 

    outvalue=''
    x=0 



    if col=='open':
        x=1
    if col=='high':
        x=2
    if col=='low':
        x=3
    if col=='close':
        x=4
    if col=='volume':
        x=5
    if col=='adj close':
        x=6



       csvfile = open(filename,"r")
       rows = csv.reader(csvfile, delimiter=',')
       for row in rows:
           if row[0] == day:
           outvalue = row[x]
           break
       csvfile.close()
       if outvalue=='':
           return ("cannot find the value")
       if x==5:
           print (outvalue)
           return int(outvalue)
       else:
           print (outvalue)
           return float(outvalue) 
