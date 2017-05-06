import csv

"""
# The program 's function read csv file of MSFT or APPL
# It reads data on each day and make buy and sell decision from prior 21 days close avg
# Program start from the past and end to the current day
"""

stock='MSFT'  
#global cvsStockActivies  #stock,share, price, date
global sellingRatio
sellingRatio =1.10
global buyRatio
buyRatio = .90
money =1000.0
stockHolding =0.0

def main():
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
    alg1_balance = alg_moving_avg(filename)



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
        dateList.append((row[0]))
        lowList.append((row[3]))
        highList.append((row[2]))
        closeList.append((row[4]))
    csvfile.close()
     
    # for index in range(len(closeList),len(closeList)-1):
    for index in range(len(closeList)-21,1,-1):       
        daysSum = 0.0
        for x in range(index+1, index+21):
            closePrice = float(closeList[x])
            daysSum = daysSum + closePrice
        buyOrSell(daysSum,dateList[index],lowList[index], highList[index])
    # selling the remain stock if any at the high price of the day  highList[0]
    if stockHolding > 0:
        cash = stockHolding*float(highList[1])
    return 0,round(cash,2)
    

def buyOrSell(sumOfClosePrice, exeDate, exeLow, exeHigh):   
    buyingPrice = (sumOfClosePrice/20)*buyRatio
    sellingPrice = (sumOfClosePrice/20)*sellingRatio
    global stockHolding
    global money
    if buyingPrice < float(exeHigh) and buyingPrice > float(exeLow):
        if money > 0:
            stockHolding = money/float(exeLow)          
            money=0.0
    elif sellingPrice > float(exeLow) and sellingPrice < float(stockHolding) :
        if stockHolding > 0:
            money = stockHolding*float(exeHigh)
            stockHolding = 0
           
   

if __name__=="__main__":
    main()


        

   

