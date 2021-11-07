'''This file is going to be used as a sample test
 bed for the functionality needed to plot coordinates
 on a map for the Coral Bleaching application. Everything
 is subject to change.'''

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

coral_map = gpd.read_file('shapeMap\Florida Shore + Reef Map.shp')
df = pd.read_csv('BW_2014_Florida.csv', encoding='ISO-8859-1')


def generate_bleach_map(year_df, coral_map):

    geometry = [Point(xy)
                for xy in zip(year_df['GIS Longitude'], year_df['GIS Latitude'])]
    geo_df = gpd.GeoDataFrame(year_df, crs='epsg:4326', geometry=geometry)

    fig, ax = plt.subplots(figsize=(10, 10))
    coral_map.plot(ax=ax, alpha=.4, color="black")

    geo_df[geo_df['Bleaching?'] == 'YES'].plot(
        ax=ax, markersize=20, color='green', marker='o', label='Yes')
    geo_df[geo_df['Bleaching?'] == 'NO'].plot(
        ax=ax, markersize=20, color='red', marker='x', label='No')

    plt.legend(prop={'size' : 10})
    fig.suptitle('Bleaching reports from selected year', fontsize=16)
    plt.show()


generate_bleach_map(df, coral_map)