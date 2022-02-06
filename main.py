"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#-------------------LOGIN---------------------------------#
username = "Manager123"
password = "lif3stor3"
tries = 0; Acces = False

"""
while not Acces:
    tries += 1

    if tries == 4:
        exit()
    if input('Username: ') == username and input('Password: ') == password:
        Acces = True
        print('Acces Granted')
    else:
        print(f'You have {3 - tries} tries lefts')
"""
#-------------------------SALES--------------------------------#
soldproduct = []; timesold = []

soldproduct = [sale[1] for sale in lifestore_sales]

for sale in lifestore_products: #Creating a nested list
    nested=[]
    timesold.append(nested)
    for k in range(1):
        nested.append(sale[0])
        nested.append(sale[1])
        nested.append(soldproduct.count(sale[0])) #Counting times sold
        nested.append(sale[-2])

def Sort(timesold): #timesold is [id_product, name, time_sold, category]
    timesold.sort(key = lambda x: x[2])
    return timesold

timesold = Sort(timesold) # Ascendant order

print("\n MOST SOLD PRODUCTS")
for i in [-1,-2,-3,-4,-5]:
    print( F'ID: {timesold[i][0]}\t NAME: {timesold[i][1]}\t SALES: {timesold[i][2]}' )

#print("\n LEAST SOLD PRODUCTS")

#for i in range(0,5):
#    print( F'ID: {timesold[i][0]}\t NAME: {timesold[i][1]}\t SALES: {timesold[i][2]}' )

#-------------------------SALES PER CATERGORY--------------------------------#
categories= []
processors = []; gpus = []; motherboards = []; drives = []; usb = []; screens = []; speakers = []; headphones = []

categories= [item[-2] for item in lifestore_products]

categories = list(dict.fromkeys(categories))

for item in timesold:
    if categories[0] in item:
        processors.append(item[:3])
    elif categories[1] in item:
        gpus.append(item[:3])
    elif categories[2] in item:
        motherboards.append(item[:3])
    elif categories[3] in item:
        drives.append(item[:3])
    elif categories[4] in item:
        usb.append(item[:3])
    elif categories[5] in item:
        screens.append(item[:3])
    elif categories[6] in item:
        speakers.append(item[:3])
    elif categories[7] in item:
        headphones.append(item[:3])

print("\n LEAST SOLD PROCESSORS")
for i in range(5):
    print(f"ID: {processors[i][0]}\t NAME: {processors[i][1]}\t TIMES SOLD: {processors[i][-1]}")

print("\n LEAST SOLD GPUS")
for i in range(5):
    print(f"ID: {gpus[i][0]}\t NAME: {gpus[i][1]}\t TIMES SOLD: {gpus[i][-1]}")

print("\n LEAST SOLD MOTHERBOARDS")
for i in range(5):
    print(f"ID: {motherboards[i][0]}\t NAME: {motherboards[i][1]}\t TIMES SOLD: {motherboards[i][-1]}")

print("\n LEAST SOLD DRIVES")
for i in range(5):
    print(f"ID: {drives[i][0]}\t NAME: {drives[i][1]}\t TIMES SOLD: {drives[i][-1]}")

print("\n LEAST SOLD USB")
for i in range(2):
    print(f"ID: {usb[i][0]}\t NAME: {usb[i][1]}\t TIMES SOLD: {usb[i][-1]}")

print("\n LEAST SOLD SCREENS")
for i in range(5):
    print(f"ID: {screens[i][0]}\t NAME: {screens[i][1]}\t TIMES SOLD: {screens[i][-1]}")

print("\n LEAST SOLD SPEAKERS")
for i in range(5):
    print(f"ID: {speakers[i][0]}\t NAME: {speakers[i][1]}\t TIMES SOLD: {speakers[i][-1]}")

print("\n LEAST SOLD HEADPHONES")
for i in range(5):
    print(f"ID: {headphones[i][0]}\t NAME: {headphones[i][1]}\t TIMES SOLD: {headphones[i][-1]}")

#-------------------------SEARCHES--------------------------------#
searchedproduct = []; timesearched = []

searchedproduct = [search[1] for search in lifestore_searches]

for search in lifestore_products: #Creating a nested list
    nested=[]
    timesearched.append(nested)
    for k in range(1):
        nested.append(search[0]) #Saving ID
        nested.append(search[1]) #Saving Name
        nested.append(searchedproduct.count(search[0])) #Counting times searched
        nested.append(search[-2]) #Saving Category
        
def Sort(timesearched):
    timesearched.sort(key = lambda x: x[2])
    return timesearched

timesearched = Sort(timesearched)

print("\n MOST SEARCHED PRODUCTS")
for i in [-1,-2,-3,-4,-5]:
    print( F'ID: {timesearched[i][0]}\t NAME: {timesearched[i][1]}\t SEARCHES: {timesearched[i][-1]}' )

#print("\n LEAST SEARCHED PRODUCTS")
#for i in range(0,10):
#    print( F'ID: {timesearched[i][0]}\t NAME: {timesearched[i][1]}\t SEARCHES: {timesearched[i][-1]}' )

#-------------------------SEARCHES PER CATERGORY--------------------------------#
processors = []; gpus = []; motherboards = []; drives = []; usb = []; screens = []; speakers = []; headphones = []

for item in timesearched:
    if categories[0] in item:
        processors.append(item[:3])
    elif categories[1] in item:
        gpus.append(item[:3])
    elif categories[2] in item:
        motherboards.append(item[:3])
    elif categories[3] in item:
        drives.append(item[:3])
    elif categories[4] in item:
        usb.append(item[:3])
    elif categories[5] in item:
        screens.append(item[:3])
    elif categories[6] in item:
        speakers.append(item[:3])
    elif categories[7] in item:
        headphones.append(item[:3])

print("\n LEAST SEARCHED PROCESSORS")
for i in range(9):
    print(f"ID: {processors[i][0]}\t NAME: {processors[i][1]}\t TIMES SEARCHED: {processors[i][-1]}")

print("\n LEAST SEARCHED GPUS")
for i in range(10):
    print(f"ID: {gpus[i][0]}\t NAME: {gpus[i][1]}\t TIMES SEARCHED: {gpus[i][2]}")

print("\n LEAST SEARCHED MOTHERBOARDS")
for i in range(10):
    print(f"ID: {motherboards[i][0]}\t NAME: {motherboards[i][1]}\t TIMES SEARCHED: {motherboards[i][-1]}")

print("\n LEAST SEARCHED DRIVES")
for i in range(10):
    print(f"ID: {drives[i][0]}\t NAME: {drives[i][1]}\t TIMES SEARCHED: {drives[i][-1]}")

print("\n LEAST SEARCHED USB")
for i in range(2):
    print(f"ID: {usb[i][0]}\t NAME: {usb[i][1]}\t TIMES SEARCHED: {usb[i][-1]}")

print("\n LEAST SEARCHED SCREENS")
for i in range(10):
    print(f"ID: {screens[i][0]}\t NAME: {screens[i][1]}\t TIMES SEARCHED: {screens[i][-1]}")

print("\n LEAST SEARCHED SPEAKERS")
for i in range(10):
    print(f"ID: {speakers[i][0]}\t NAME: {speakers[i][1]}\t TIMES SEARCHED: {speakers[i][-1]}")

print("\n LEAST SEARCHED HEADPHONES")
for i in range(10):
    print(f"ID: {headphones[i][0]}\t NAME: {headphones[i][1]}\t TIMES SEARCHED: {headphones[i][-1]}")


#----------------------REVIEWS--------------------------#
tempsum=0; totalscore = []; averagescore = []

for i in range(0,len(lifestore_products)): 
    for k in range(0,len(lifestore_sales)):
        if lifestore_sales[k][1]==timesold[i][0]:
            tempsum += lifestore_sales[k][2] #Adding up review scores
    
    totalscore.append(tempsum)
    tempsum=0

for review in lifestore_products: #Creating a nested list
    nested=[]
    if timesold[review[0]-1][2] > 0: #Obtaining reviews from products sold at least once
        averagescore.append(nested)
        for k in range(1):
            nested.append(review[0])
            nested.append(review[1])
            nested.append(timesold[review[0]-1][2]) #Times reviewed
            nested.append(totalscore[review[0]-1]/timesold[review[0]-1][2]) #Obtaining average

def Sort(averagescore):
    averagescore.sort(key = lambda x: x[-1])
    return averagescore

averagescore = Sort(averagescore)

print("\n BEST RATED PRODUCTS")
for i in range(-1,-11,-1):
    print( F'ID: {averagescore[i][0]}\t NAME: {averagescore[i][1]}\t SCORE: {averagescore[i][-1]}\t TIMES REVIEWED: {averagescore[i][2]}' )

print("\n WORST RATED PRODUCTS")
for i in range(0,10):
    print( F'ID: {averagescore[i][0]}\t NAME: {averagescore[i][1]}\t SCORE: {averagescore[i][-1]}\t TIMES REVIEWED: {averagescore[i][2]}' )

#----------------------SALES PER MONTH--------------------------#
from datetime import datetime; import calendar
date = [sale[3] for sale in lifestore_sales]
date.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y')) # Sort the dates in order 

month =calendar.month_name[1:]

refundeditem = []; totalrefunds = 0; averageticket = []
totalsales = 0; monthsales = [0]*12;  monthprofit = [0]*12

soldproduct = [sale[1] for sale in lifestore_sales]

for i in range(0,len(lifestore_sales)):
    if int(lifestore_sales[i][-1]) == 0:                    #Verifying it was not a refund
        totalsales+=lifestore_products[soldproduct[i]][2]   #Adding up the total sales
        if "/01/" in date[i]:
            monthprofit[0]+=lifestore_products[soldproduct[i]][2]
            monthsales[0]+=1
        elif "/02/" in date[i]:
            monthprofit[1]+=lifestore_products[soldproduct[i]][2]
            monthsales[1]+=1
        elif "/03/" in date[i]:
            monthprofit[2]+=lifestore_products[soldproduct[i]][2]
            monthsales[2]+=1
        elif "/04/" in date[i]:
            monthprofit[3]+=lifestore_products[soldproduct[i]][2]
            monthsales[3]+=1
        elif "/05/" in date[i]:
            monthprofit[4]+=lifestore_products[soldproduct[i]][2]
            monthsales[4]+=1
        elif "/06/" in date[i]:
            monthprofit[5]+=lifestore_products[soldproduct[i]][2]
            monthsales[5]+=1
        elif "/07/" in date[i]:
            monthprofit[6]+=lifestore_products[soldproduct[i]][2]
            monthsales[6]+=1
        elif "/08/" in date[i]:
            monthprofit[7]+=lifestore_products[soldproduct[i]][2]
            monthsales[7]+=1
        elif "/09/" in date[i]:
            monthprofit[8]+=lifestore_products[soldproduct[i]][2]
            monthsales[8]+=1
        elif "/10/" in date[i]:
            monthsales[9]+=lifestore_products[soldproduct[i]][2]
            monthsales[9]+=1
        elif "/11/" in date[i]:
            monthprofit[10]+=lifestore_products[soldproduct[i]][2]
            monthsales[10]+=1
        elif "/12/" in date[i]:
            monthprofit[11]+=lifestore_products[soldproduct[i]][2]
            monthsales[11]+=1
    else:
        refundeditem.append(soldproduct[i])                 #ID product refunded
        totalrefunds+=lifestore_products[soldproduct[i]][2] #Total lost in refunds

for i in range(12): 
    if monthsales[i] > 0:
        averageticket.append(monthprofit[i]/monthsales[i]) #Obtaining average
    else:
        averageticket.append(0)

salesxmonth = [list(l) for l in zip(month, monthprofit, monthsales, averageticket)]

def Sort(salesxmonth): #Sort for profit
    salesxmonth.sort(key = lambda x: x[1])
    return salesxmonth
salesxmonth = Sort(salesxmonth)

print("\n MOST PROFITABLE MONTHS")
for i in [-1,-2,-3,-4,-5]:
    print( F'MONTH: {salesxmonth[i][0]}\t PROFIT: {"${:,.2f}".format(salesxmonth[i][1])}\t SALES: {salesxmonth[i][2]}\t AVERAGE: {salesxmonth[i][-1]}' )

def Sort(salesxmonth): #Sort for sales
    salesxmonth.sort(key = lambda x: x[2])
    return salesxmonth
salesxmonth = Sort(salesxmonth)

print("\n MOST SALES PER MONTHS")
for i in [-1,-2,-3,-4,-5]:
    print( F'MONTH: {salesxmonth[i][0]}\t PROFIT: {"${:,.2f}".format(salesxmonth[i][1])}\t SALES: {salesxmonth[i][2]}\t AVERAGE: {salesxmonth[i][-1]}' )

def Sort(salesxmonth): #Sort for average ticket
    salesxmonth.sort(key = lambda x: x[-1])
    return salesxmonth
salesxmonth = Sort(salesxmonth)

print("\n HIGHEST AVERAGE TICKET PER MONTH")
for i in [-1,-2,-3,-4,-5]:
    print( F'MONTH: {salesxmonth[i][0]}\t PROFIT: {"${:,.2f}".format(salesxmonth[i][1])}\t SALES: {salesxmonth[i][2]}\t AVERAGE: {salesxmonth[i][-1]}' )

print(salesxmonth)
