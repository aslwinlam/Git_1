import csv
def getQuote(param1, param2, param3):
    outvalue=''
    x=0
    # might need to map the type of code to the name of the stock to the name of file
    # if param1="apple", param = "apples.csv"...
    
    if param2=='open':
        x=1
    if param2=='close':
      	x=2
    csvfile = open(param,"rb") 
    row = csv.reader(csvfile, delimiter=',')
    for row in row:
            # assume row[0] is the Date column in the CSV file
            # and param3 is the Date the function want to find
        if row[0] == param3:
            outvalue = row[x]
            break
        csvfile.close()
        # add this in case the user input a date where it is not on the csv file
        if outvalue=="":
            return "cannot find the value"
        if x==0:
            return int(outvalue)
        else:
            return float(outvalue)
