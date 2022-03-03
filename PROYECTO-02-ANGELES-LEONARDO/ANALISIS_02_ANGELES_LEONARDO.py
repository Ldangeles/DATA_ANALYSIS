import pandas as pd
from collections import Counter

database = pd.read_csv( 'synergy_logistics_database.csv')

routes = [i +"-"+ j for i, j in zip(list(database["origin"]), list(database["destination"]))] #Joining origin and destination
database['route'] = routes

#print(database)

routes_dicc = list(dict.fromkeys(routes)) #Obtaining a list with all the routes
routes_counter = Counter(routes) #Obtaining the times this route was used
routes_sorted,route_profit = [],[]

for route in routes_dicc: #Creating a nested list
    nested=[]
    routes_sorted.append(nested)
    for k in range(1):
        nested.append(route)
        nested.append(routes_counter[route])

def Sort(routes_sorted): #Sorting the routes
    routes_sorted.sort(key = lambda x: x[1], reverse=True)
    return routes_sorted
routes_sorted = Sort(routes_sorted) # Descendant order

print("\n MOST USED ROUTES")
tempsum = 0
for i in range(0,10):
    print( F'ROUTE: {routes_sorted[i][0]}\t TIMES USED: {routes_sorted[i][1]}')
    tempsum += routes_sorted[i][1]
    if i >= 9:
        print(f'\nTOP 10 ROUTES SUMMED UP: {"{:,.0f}".format(tempsum)}\t PERCENTAGE OF EXPORTATIONS: {"{:,.2f}%".format(100*tempsum/len(routes))}')

routes_transport_profit = list(zip(list(database["route"]), list(database["transport_mode"]),list(database["total_value"])))

tempsum = 0    
for route in routes_dicc:
    for i in range(0,len(list(routes_transport_profit))):
        if route == routes_transport_profit[i][0]:
            tempsum += routes_transport_profit[i][-1]
    nested=[]
    route_profit.append(nested)
    for k in range(1):
        nested.append(route)
        nested.append(tempsum)
    tempsum = 0

def Sort(route_profit): #Sorting the routes
    route_profit.sort(key = lambda x: x[-1], reverse=True)
    return route_profit
route_profit = Sort(route_profit) # Descendant order

print("\n MOST PROFITABLE ROUTES")
tempsum = 0
for i in range(0,10):
    print( F'ROUTE: {route_profit[i][0]}\t PROFITS: {"${:,.0f}".format(route_profit[i][-1])}')
    tempsum += route_profit[i][-1]
    if i >= 9:
        print(f'\nTOP 10 ROUTES SUMMED UP: {"${:,.0f}".format(tempsum)}\t PERCENTAGE OF PROFITS: {"{:,.2f}%".format(100*tempsum/database["total_value"].sum())}')

#------------------------------TRANSPORT----------------------------#
transport_dicc = list(dict.fromkeys(database["transport_mode"])) #Obtaining a list with all transports
transport_profit = []

tempsum = 0
for transport in transport_dicc:
    for i in range(0,len(list(routes_transport_profit))):
        if transport == routes_transport_profit[i][1]:
            tempsum += routes_transport_profit[i][-1]
    nested=[]
    transport_profit.append(nested)
    for k in range(1):
        nested.append(transport)
        nested.append(tempsum)
    tempsum = 0

def Sort(transport_profit): #Sorting the routes
    transport_profit.sort(key = lambda x: x[-1], reverse=True)
    return transport_profit
transport_profit = Sort(transport_profit) # Descendant order

print("\n MOST PROFITABLE TRANSPORT")
tempsum = 0
for i in range(0,4):
    print( F'TRANSPORT: {transport_profit[i][0]}\t PROFITS: {"${:,.0f}".format(transport_profit[i][-1])}')
    if i >= 3:
        print(f'\nMOST PROFITABLE TRANSPORT: {"${:,.0f}".format(transport_profit[0][-1])}\t PERCENTAGE OF PROFITS: {"{:,.2f}%".format(100*transport_profit[0][-1]/database["total_value"].sum())}')

#----------------------------------EXPORTS-----------------------------------#

origin_dicc = list(dict.fromkeys(database["origin"])) #Obtaining a list with all the origins
origin_dest_profit = list(zip(list(database["origin"]), list(database["destination"]),list(database["total_value"])))

origin_profit=[]

tempsum = 0
for origin in origin_dicc:
    for i in range(0,len(list(origin_dest_profit))):
        if origin == origin_dest_profit[i][0]:
            tempsum += origin_dest_profit[i][-1]
    nested=[]
    origin_profit.append(nested)
    for k in range(1):
        nested.append(origin)
        nested.append(tempsum)
    tempsum = 0

def Sort(origin_profit): #Sorting the routes
    origin_profit.sort(key = lambda x: x[-1], reverse=True)
    return origin_profit
origin_profit = Sort(origin_profit) # Descendant order

print("\n MOST PROFITABLE ORIGIN")
tempsum = 0
for i in range(0,8):
    print( F'ORIGIN: {origin_profit[i][0]}\t PROFITS: {"${:,.0f}".format(origin_profit[i][-1])}')
    tempsum += origin_profit[i][-1]
    if i >= 7:
        print(f'\nMOST PROFITABLE ORIGINS SUMMED UP: {"${:,.0f}".format(tempsum)}\t PERCENTAGE OF PROFITS: {"{:,.2f}%".format(100*tempsum/database["total_value"].sum())}')

#----------------------------------IMPORTS-----------------------------------#
destination_dicc = list(dict.fromkeys(database["destination"])) #Obtaining a list with all the destinations

destination_profit=[]

tempsum = 0
for destination in destination_dicc:
    for i in range(0,len(list(origin_dest_profit))):
        if destination == origin_dest_profit[i][1]:
            tempsum += origin_dest_profit[i][-1]
    nested=[]
    destination_profit.append(nested)
    for k in range(1):
        nested.append(destination)
        nested.append(tempsum)
    tempsum = 0

def Sort(destination_profit): #Sorting the routes
    destination_profit.sort(key = lambda x: x[-1], reverse=True)
    return destination_profit
destination_profit = Sort(destination_profit) # Descendant order

print("\n MOST PROFITABLE DESTINATION")
tempsum = 0
for i in range(0,13):
    print( F'DESTINATION: {destination_profit[i][0]}\t PROFITS: {"${:,.0f}".format(destination_profit[i][-1])}')
    tempsum += destination_profit[i][-1]
    if i >= 12:
        print(f'\nMOST PROFITABLE DESTINATIONS SUMMED UP: {"${:,.0f}".format(tempsum)}\t PERCENTAGE OF PROFITS: {"{:,.2f}%".format(100*tempsum/sum(database["total_value"]))}')
