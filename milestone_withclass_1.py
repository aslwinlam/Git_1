"""
The program 's function read csv file of MSFT or APPL
It buy stock and sell the stock each day (depend on the price) to make $100 profit
After sale of the stock, it will attempt to buy the stock back with the 3%, 5%, 7%, 9% (margin) less then the sold price.BaseException
If no purchase cannot be reach for 5 days with the above margin, it will purchase at market price (no the discount/margin price)
Program start from the past and end to the current day


"""

import csv

# import tradinglib
from tradinglib import RowOfStockinf


ROWSOFSTOCKINF = []  # ..........List of objects (rows of trading)


def main():
    """ Main module"""
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
   # alg_mov = alg_moving_avg(filename)
    alg1_balance = alg_mine(filename)
    print(alg1_balance)


def alg_mine(filename):
    """ This function loop from the bottom and day trade the stock
    Variables for computation :-
        AAPL.csv or MSFT.csv (per user input)
        RowOfStockinf.cash (looped and store in accordance to buyMargin) - all start with 2000.0
        RowOfStockinf.numberOfStock (looped and store in accordance to buyMargin)
        RowOfStockinf.buyMargin (hardcode to loop through)

    Output :
        Day trading result for each buyMargin (4)
    """
    
    csvfile = open(filename, "r")
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:   # read spread sheet row into object
        stock_inf_obj = RowOfStockinf(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # create Object
        ROWSOFSTOCKINF.append(stock_inf_obj)    
    csvfile.close()

    # the trading is on the 21 days counting backward
# Buy $2000 of stock base on the the last row's lowest price

# loop the margin here ... buyMargin[0]...[3]
    for x in range(0,4,1):
    #------------->BLOCK FOR SET FOR A buyMargin
        lastRow =len(ROWSOFSTOCKINF) - 1
        lowPrice = float(ROWSOFSTOCKINF[lastRow].trade_low)
        highPrice= float(ROWSOFSTOCKINF[lastRow].trade_high)    
        avgPrice = (lowPrice+highPrice)/2    
        pricePay = avgPrice
        RowOfStockinf.numOfStock[x] = RowOfStockinf.cash[x]/avgPrice # First transaction use avg price
        RowOfStockinf.cash[x] = 0.0
        priceTosell = pricePay + 100/RowOfStockinf.numOfStock[x]
        executePrice = 0.0
    # Day trading program
        missingBuycounter = 0
        missingSellcounter = 0
    #<------ BLOCK FOR SET FOR A buyMargin
        for index in range(len(ROWSOFSTOCKINF) - 2, 1, -1):
            toDaylowPrice = float(ROWSOFSTOCKINF[index].trade_low)
            toDayHighPrice = float(ROWSOFSTOCKINF[index].trade_high)
            executePrice = (toDaylowPrice + toDayHighPrice) / 2
            # SELL CONDITION
            if RowOfStockinf.cash[x] == 0.0:      # means there are stock to sell
                if priceTosell > toDaylowPrice:               # do my selling
                    RowOfStockinf.cash[x] = float(RowOfStockinf.numOfStock[x] * priceTosell)  # sell it with only daily margin $100
                    RowOfStockinf.numOfStock[x] = 0.0
                    priceToBuy = priceTosell * RowOfStockinf.buyMargin[x]  # buy it with only daily margin
                    missingSellcounter = 0
                    RowOfStockinf.numOfSales[x] =RowOfStockinf.numOfSales[x]+1
                else:
                    missingSellcounter = missingSellcounter + 1
            if RowOfStockinf.numOfStock[x] == 0.0:
                if priceToBuy < toDayHighPrice and priceToBuy > toDaylowPrice:
                    # do my buy
                    RowOfStockinf.numOfStock[x] =  RowOfStockinf.cash[x]/ priceToBuy
                    RowOfStockinf.cash[x] = 0.0
                    priceTosell = priceToBuy + 100/RowOfStockinf.numOfStock[x]
                    missingBuycounter = 0
                elif missingBuycounter > 4 :   #
                    RowOfStockinf.numOfStock[x] =  RowOfStockinf.cash[x]/ executePrice  # replace priceToBuy with executePrice
                    RowOfStockinf.cash[x] = 0.0
                    priceTosell = executePrice + 100.0/RowOfStockinf.numOfStock[x]
                    missingBuycounter = 0  
                  #  print('catch up ' + str(index) + "  price to sell " + str(priceTosell) +'....'+str(x))
                  #  print('number of stocks ' +str(RowOfStockinf.numOfStock[x]))                 
                else:
                    missingBuycounter = missingBuycounter + 1
                        
        

   # Trading_summary = "Buy stock with 3% less than selling price...." +str(((RowOfStockinf.numOfStock[0]*executePrice)+RowOfStockinf.cash[0])) +"\n"
   # Trading_summary = "Buy stock with 5% less than selling price...." +str(((RowOfStockinf.numOfStock[1]*executePrice)+RowOfStockinf.cash[1])) +"\n" + Trading_summary
    # Trading_summary = "Buy stock with 7% less than selling price...." +str(((RowOfStockinf.numOfStock[2]*executePrice)+RowOfStockinf.cash[2])) +"\n" + Trading_summary
    # Trading_summary = "Buy stock with 9% less than selling price...." +str(((RowOfStockinf.numOfStock[3]*executePrice)+RowOfStockinf.cash[3])) +"\n" + Trading_summary

    return int(RowOfStockinf.numOfStock[0]), float(RowOfStockinf.cash[0])


global sellingRatio
sellingRatio =1.10
global buyRatio
buyRatio = .90
money =2000.0
stockHolding =0.0


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
    cash = money
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


       


main()
