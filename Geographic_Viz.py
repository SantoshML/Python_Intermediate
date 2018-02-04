# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:14:53 2018

@author: Santosh Kumar
"""

##-------------------Geographical Data Plotting--------------#####
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

os.getcwd()
os.chdir("./airports.csv")

airports = pd.read_csv("airports.csv")

fig,ax = plt.subplots(figsize = (15,20))

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()

ax.set_title("Scaled Up Earth With Coastlines")

plt.show()

#To better understand the flight routes, we can draw great circles #to connect starting and ending locations on a map. A great circle #is the shortest circle connecting 2 points on a sphere.

import pandas as pd

geo_routes = pd.read_csv("geo_routes.csv")
geo_routes.info()

geo_routes.head()

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

#Creating a Function to connect airports

def create_great_circles(Dataset):
    for ind,row in Dataset.iterrows():
        if abs(row['end_lat'] - row['start_lat']) < 180 and abs(row['end_lon'] - row['start_lon']) < 180:
            m.drawgreatcircle(lon1 = row['start_lon'],lat1 = row['start_lat'],lon2 = row['end_lon'] ,lat2 = row['end_lat'])


     
    

    
dfw = geo_routes.loc[geo_routes["source"] == "DFW",:]   
create_great_circles(dfw)
plt.show()