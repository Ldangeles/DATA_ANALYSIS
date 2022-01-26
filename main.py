"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#-------------------------SALES--------------------------------#
soldproduct = []; refundeditem = []; 
totalsales=0; totalrefunds=0
timesold = []; productsnotsold = []; mostsoldproduct = []; leastsoldproduct = []

def Extract(soldproduct):
    return [item[1] for item in lifestore_sales]

soldproduct = Extract(soldproduct)

for i in range(0,len(soldproduct)):
    if int(lifestore_sales[i][-1]) == 0:                    #Verifying it was not a refund
        totalsales+=lifestore_products[soldproduct[i]][2]   #Adding up the total sales
    else:
        refundeditem.append(soldproduct[i])                 #ID product refunded
        totalrefunds+=lifestore_products[soldproduct[i]][2] #Total lost in refunds

#print("El total de ventas es de $" + str(totalsales)) #Total of sales
#print("El total de devoluciones es de $" + str(totalrefunds)) #Total of refunds

for i in range(0,len(lifestore_products)):
    timesold.append(soldproduct.count(i+1))             #Zero doesnt count
    if timesold[i] == 0:
        productsnotsold.append(lifestore_products[i][1])

templist = timesold.copy()                         #Templist         
print("\n MOST SOLD PRODUCTS")
for i in range(0,5):                                    #Obtaining the 5 most sold products                               
    max_idx = templist.index(max(templist))
    mostsoldproduct.append(max_idx)
    templist[max_idx]=0                                 #Erasing last most sold product
    print("ID: "+str(lifestore_products[mostsoldproduct[i]][0])+"\t NAME: "+lifestore_products[mostsoldproduct[i]][1])

templist = timesold.copy()                        #Reset templist 
print("\n LEAST SOLD PRODUCTS")
for i in range(0,5):                                    #Obtaining the 5 least sold products
    min_idx = templist.index(min(templist))
    leastsoldproduct.append(min_idx)
    templist[min_idx]=1000                              #Erasing last least sold product
    print("ID: "+str(lifestore_products[leastsoldproduct[i]][0])+"\t NAME: "+lifestore_products[leastsoldproduct[i]][1])


#-------------------------SEARCHES--------------------------------#
searchedproduct = []; timesearched = []; mostsearchedproduct = []; leastsearchedproduct = []

def Extract(searchedproduct):
    return [item[1] for item in lifestore_searches]

searchedproduct = Extract(searchedproduct)

for i in range(0,len(lifestore_products)):
    timesearched.append(searchedproduct.count(i+1))

templist = timesearched.copy()                          #Templist
print("\n MOST SEARCHED PRODUCTS")
for i in range(0,10):                               #Obtaining the 10 most searched products
    max_idx = templist.index(max(templist))
    mostsearchedproduct.append(max_idx)
    templist[max_idx]=0                             #Erasing last most searched product
    print("ID: "+str(lifestore_products[mostsearchedproduct[i]][0])+"\t NAME: "+lifestore_products[mostsearchedproduct[i]][1])

templist = timesearched.copy()                        #Reset templist
print("\n LEAST SEARCHED PRODUCTS")
for i in range(0,10):                               #Obtaining the 10 least searched products
    min_idx = templist.index(min(templist))
    leastsearchedproduct.append(min_idx)
    templist[min_idx]=1000                          #Erasing last least searched product
    print("ID: "+str(lifestore_products[leastsearchedproduct[i]][0])+"\t NAME: "+lifestore_products[leastsearchedproduct[i]][1])

#print(searchedproduct); print(timesearched)

#----------------------REVIEWS--------------------

#print(timesold)
tempsum=0; totalscore = [];averagescorewID = []; ratedproducts = []
bestratedproduct = []; worstratedproduct = []

for i in range(0,len(lifestore_products)): #Adding up review scores
    for k in range(0,len(lifestore_sales)):
        if lifestore_sales[k][1]==i+1:
            tempsum += lifestore_sales[k][2]
    
    totalscore.append(tempsum)
    tempsum=0

for i in range(0,len(lifestore_products)):
    nested = []
    averagescorewID.append(nested)
    if timesold[i]>0:
        for k in range(1):
            nested.append(i+1)
            nested.append(totalscore[i]/timesold[i])
    else:
        for l in range(1):
            nested.append(i+1)
            nested.append(-1)

for i in range(0,len(averagescorewID)):
    if averagescorewID[i][1]>0:
        ratedproducts.append(averagescorewID[i][1])

templist = ratedproducts.copy()  

print("\n BEST RATED PRODUCTS")
for i in range(0,5):                               #Obtaining the 10 most searched products
    max_idx = templist.index(max(templist))
    bestratedproduct.append(max_idx)
    templist[max_idx]=0                             #Erasing last most searched product
    print("ID: "+str(lifestore_products[bestratedproduct[i]][0])+"\t NAME: "+lifestore_products[bestratedproduct[i]][1])

templist = ratedproducts.copy() 

print("\n WORST RATED PRODUCTS")
for i in range(0,5):                               #Obtaining the 5 best rated products
    min_idx = templist.index(min(templist))
    worstratedproduct.append(min_idx)
    templist[min_idx]=1000                            #Erasing last most searched product
    print("ID: "+str(lifestore_products[worstratedproduct[i]][0])+"\t NAME: "+lifestore_products[worstratedproduct[i]][1])

