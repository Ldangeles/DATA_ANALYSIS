"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from monthsales import totalsales, monthsales, date
import copy
#-------------------Login--------------
username = "Manager123"
password = "lif3stor3"

if username == input("Username: "):
    if password == input("Password: "):
        print("pasaste")

#-------------------------SALES--------------------------------#
soldproduct = []; timesold = []; productsnotsold = []; 
mostsoldproduct = []; leastsoldproduct = []

def Extract(soldproduct):
    return [item[1] for item in lifestore_sales]

soldproduct = Extract(soldproduct)

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
    print("ID: "+str(lifestore_products[mostsoldproduct[i]][0])+"\t NAME: "+lifestore_products[mostsoldproduct[i]][1] 
    + "\t TIMES: " + str(timesold[mostsoldproduct[i]]))

templist = timesold.copy()                        #Reset templist 
print("\n LEAST SOLD PRODUCTS")
for i in range(0,5):                                    #Obtaining the 5 least sold products
    min_idx = templist.index(min(templist))
    leastsoldproduct.append(min_idx)
    templist[min_idx]=1000                              #Erasing last least sold product
    print("ID: "+str(lifestore_products[leastsoldproduct[i]][0])+"\t NAME: "+lifestore_products[leastsoldproduct[i]][1]+
    "\t TIMES: " + str(timesold[leastsoldproduct[i]]))


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
    print("ID: "+str(lifestore_products[mostsearchedproduct[i]][0])+"\t NAME: "+lifestore_products[mostsearchedproduct[i]][1] 
    + "\t TIMES: " + str(templist[mostsearchedproduct[i]]))
    templist[max_idx]=0                             #Erasing last most searched product

templist = timesearched.copy()                        #Reset templist
print("\n LEAST SEARCHED PRODUCTS")
for i in range(0,10):                               #Obtaining the 10 least searched products
    min_idx = templist.index(min(templist))
    leastsearchedproduct.append(min_idx)
    print("ID: "+str(lifestore_products[leastsearchedproduct[i]][0])+"\t NAME: "+lifestore_products[leastsearchedproduct[i]][1] 
    + "\t TIMES: " + str(templist[leastsearchedproduct[i]]))
    templist[min_idx]=1000                          #Erasing last least searched product

#print(searchedproduct); print(timesearched)

#----------------------REVIEWS--------------------------#

tempsum=0; totalscore = [];averagescorewID = []; ratedproducts = []
bestratedproduct = []; worstratedproduct = []

for i in range(0,len(lifestore_products)): #Adding up review scores
    for k in range(0,len(lifestore_sales)):
        if lifestore_sales[k][1]==i+1:
            tempsum += lifestore_sales[k][2]
    
    totalscore.append(tempsum)
    tempsum=0

"""
print("\n----------------")
print(totalscore)
print(timesold)
print("\n----------------")
"""

for i in range(0,len(lifestore_products)):
    nested1 = []; nested2 = []; j=0
    averagescorewID.append(nested1)

    if timesold[i]>0:
        ratedproducts.append(nested2)
        for k in range(1):
            nested1.append(i+1)
            nested1.append(totalscore[i]/timesold[i])
            nested2.append(i+1)
            nested2.append(totalscore[i]/timesold[i])
    else:
        for l in range(1):
            nested1.append(i+1)
            nested1.append(-1)

print("\n ratedproducts"); print(ratedproducts)
templist = copy.deepcopy(ratedproducts)
print("\n templist"); print(templist)

print("\n BEST RATED PRODUCTS")
for i in range(0,5):                               #Obtaining the 10 most searched products
    max_idx = templist.index(max(templist, key=lambda x: x[1]))
    bestratedproduct.append(max_idx)
    print("ID: "+ str(lifestore_products[bestratedproduct[i]][0])+"\t NAME: "+ lifestore_products[bestratedproduct[i]][1]+"\t SCORE: "+str(templist[max_idx]))
    templist[max_idx][1]=0                             #Erasing last most searched product

print("\n ratedproducts"); print(ratedproducts)
templist = copy.deepcopy(ratedproducts)
print("\n templist"); print(templist)

print("\n WORST RATED PRODUCTS")
for i in range(0,5):                               #Obtaining the 5 best rated products
    min_idx = templist.index(min(templist, key=lambda x: x[1]))
    worstratedproduct.append(min_idx)
    print("ID: "+str(lifestore_products[worstratedproduct[i]][0])+"\t NAME: "+lifestore_products[worstratedproduct[i]][1]+"\t SCORE: "+str(templist[min_idx]))
    templist[min_idx][1]=1000                            #Erasing last most searched product

#----------------------SALES--------------------------#

print("\nThe total revenue from "+date[0]+" to "+date[-1]+" is: "+ str(totalsales))
print("The average revenue per month is: " + str(totalsales/12))

print("\n MOST PROFITABLE MONTHS: ")

for i in [0,1,2]:
    if monthsales.index(max(monthsales)) == 0:
        print("January sales: "+ str(monthsales[0]))
        monthsales[0]=-1
    elif monthsales.index(max(monthsales)) == 1:
        print("February sales: "+ str(monthsales[1]))
        monthsales[1]=-1
    elif monthsales.index(max(monthsales)) == 2:
        print("March sales: "+ str(monthsales[2]))
        monthsales[2]=-1
    elif monthsales.index(max(monthsales)) == 3:
        print("April sales: "+ str(monthsales[3]))
        monthsales[3]=-1
    elif monthsales.index(max(monthsales)) == 4:
        print("May sales: "+ str(monthsales[4]))
        monthsales[4]=-1
    elif monthsales.index(max(monthsales)) == 5:
        print("June sales: "+ str(monthsales[5]))
        monthsales[5]=-1
    elif monthsales.index(max(monthsales)) == 6:
        print("July sales: "+ str(monthsales[6]))
        monthsales[6]=-1
    elif monthsales.index(max(monthsales)) == 7:
        print("August sales: "+ str(monthsales[7]))
        monthsales[7]=-1
    elif monthsales.index(max(monthsales)) == 8:
        print("September sales: "+ str(monthsales[8]))
        monthsales[8]=-1
    elif monthsales.index(max(monthsales)) == 9:
        print("October sales: "+ str(monthsales[9]))
        monthsales[9]=-1
    elif monthsales.index(max(monthsales)) == 10:
        print("November sales: "+ str(monthsales[10]))
        monthsales[10]=-1
    elif monthsales.index(max(monthsales)) == 11:
        print("December sales: "+ str(monthsales[11]))
        monthsales[11]=-1

