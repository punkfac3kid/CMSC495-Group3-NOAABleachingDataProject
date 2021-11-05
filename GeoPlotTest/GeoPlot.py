'''This file is going to be used as a sample test
 bed for the functionality needed to plot coordinates
 on a map for the Coral Bleaching application. Everything
 is subject to change.'''

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import geometry
from shapely.geometry import Point, Polygon

coral_map = gpd.read_file('.\shapemap\Coral_and_Hard_Bottom_Habitats_in_Florida.shp')

fig,ax = plt.subplots(figsize = (15,15))
coral_map.plot(ax = ax)


df = pd.read_csv('test_DF.csv')
crs = 'epsg:4326'
df.head()

geometry = [Point(xy) for xy in zip (df["Long"], df["Lat"])]


geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
geo_df.head()

fig.ax = plt.subplots(figsize = (15, 15))
coral_map.plot(ax=ax, alpha=.4, color="grey")

geo_df.plot(ax=ax, markersize=20, color="purple", marker="^", label="Bleach Report")
plt.show()
