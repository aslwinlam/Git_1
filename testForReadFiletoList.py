import csv

def main():
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
    alg1_balance = alg_moving_avg(filename)


def writeLog(inf):
    logFile = open('log.txt','a')
    logFile.write(inf)
    logFile.close()



def alg_moving_avg(filename):
    closeList =[]   # list to how close column from the csv file 
    dateList=[]     # list to how date column from the csv file
    highList=[]     # list to how high column from the csv file (buy/sell decison)
    lowList=[]      # list to how low column from the csv file (buy/sell decison)
   
    if filename == 'AAPL.csv':
        stock='APPL'
    csvfile = open(filename,"r")
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        dateList.append((row[0]))  # this is the first column row[0] for the Date
        lowList.append((row[3]))  # this is the 4 columns row[3] for low price
        highList.append((row[2])) # this is the 3 columns row[2] for high price 
        closeList.append((row[4])) # this is the 5 columns row[4] for close price 
    csvfile.close()
    print(closeList)  # one way to print it
    print (len(closeList)) # print number of rows in the file
    """
        THE NEXT LOOP PRINT OUT ALL ELEMENT ONE BY ONE ON THE SCREEN FOR YOU
        notice the tolal number of row is len(closeList) say 5000, but because
        the List start with "0" index not "1"  ... there the last element is 5000-1
    """
    for x in range(len(closeList)-1,0,-1):
        print("row "+ str(x) +" Closing value="+ closeList[x])

    



