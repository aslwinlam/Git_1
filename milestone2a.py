import csv

"""
The program 's function read csv file of MSFT or APPL
It reads data on each day and make buy and sell decision from prior 21 days close avg
Program start from the past and end to the current day
"""

money =1000.0     # starting $1000 - to be changes per trade 
stockHolding =0.0

def main():
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
    alg1_balance = alg_moving_avg(filename)
    print(alg1_balance)
# copy here

def alg_moving_avg(filename):
    closeList =[]   # list to how close column from the csv file 
    highList=[]     # list to how high column from the csv file (buy/sell decison)
    lowList=[]      # list to how low column from the csv file (buy/sell decison)
   
class stockdatetrading
      close,
      date,
      low,
      high
      vol


      
 class car
    engine
    transmittion
    steer wheel
    tire

 
            
fiat
an object of a car is totaya
  eninge =100hp
  transmistion = 5 speed
  

toyto = new car
toyto.engine = 1000
toyta.tramission = 5
steer wheel = 6

fiat = new car
fiat.engine = 2000
fiat.tramission = 5
fiat wheel = 43

is totay.engine > fiat.engine

groupOfrow =[]

row = 2/13/14,12313,1231,
   row[0], row[1]
    csvfile = open(filename,"r")
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        objectofrow = new stockdatetrading
        objectofrow.low= row[3]
        objectofrow.high= row[4]
        objectofrow.high= row[5]
        groupOfrow.append(objectofrow)

        
                          
        lowList.append((row[3]))
        highList.append((row[2]))
        closeList.append((row[4]))
    csvfile.close()
    
    # for index in range(len(closeList),len(closeList)-1):
    for index in range(len(closeList)-1-20,1,-1):    # the trading is on the 21 days counting backward   
        sumClosingPrice= 0.0
        for x in range(index+1, index+21):   # sum of 20 days loop 21-1
            closePrice = float(closeList[x])
            sumClosingPrice = sumClosingPrice + closePrice
        buyOrSell(sumClosingPrice,lowList[index], highList[index]) # reach the sum of 20 days here
    # Looping complete, selling the remain stock if any at the high price of the day  highList[0]
   
   cash = money
    if stockHolding > 0:
        cash = stockHolding*float(highList[1])

        
       
    return 0,cash


def buyOrSell(sumOfClosePrice, exeLow, exeHigh):   
    buyingPrice = (sumOfClosePrice/20)*.9   #  .90 want to buy low (use 10%)
    sellingPrice = (sumOfClosePrice/20)*1.1 # 1.1 want to sell high (use 10%)
    global stockHolding
    global money
    if buyingPrice < float(exeHigh) and buyingPrice > float(exeLow):
        if money > 0:
            stockHolding = money/float(exeLow)          
            money=0.0
        #    print("BUY")
    elif sellingPrice > float(exeLow) and sellingPrice < float(exeHigh) :
        if stockHolding > 0:
            money = stockHolding*float(exeHigh)
            stockHolding = 0
           # print("SELL")
           
  #<--- end copy 




        

   

