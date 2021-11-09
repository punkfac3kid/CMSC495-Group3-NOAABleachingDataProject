'''This file is going to be used as a sample test
 bed for the functionality needed to plot coordinates
 on a map for the Coral Bleaching application. Everything
 is subject to change.'''

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import geometry
from shapely.geometry import Point

coral_map = gpd.read_file('shapeMap\Florida Shore + Reef Map.shp')

df = pd.read_csv('bleach_watch_2014.csv', encoding='ISO-8859-1')
df2 = pd.read_csv('bleach_watch_2018.csv', encoding='Windows-1252')

df = df[df['GIS Longitude'].notna()]
df2 = df2[df2['GIS Longitude'].notna()]


def generate_bleach_map(year_df, coral_map, year_title):

    geometry = [Point(xy)
                for xy in zip(year_df['GIS Longitude'], year_df['GIS Latitude'])]
    geo_df = gpd.GeoDataFrame(year_df, crs='epsg:4326', geometry=geometry)

    fig, ax = plt.subplots(figsize=(10, 10))
    coral_map.plot(ax=ax, alpha=.4, color="black")

    geo_df[geo_df['Bleaching?'] == 'YES'].plot(
        ax=ax, markersize=20, color='green', marker='o', label='Yes')
    geo_df[geo_df['Bleaching?'] == 'NO'].plot(
        ax=ax, markersize=20, color='red', marker='x', label='No')

    plt.legend(prop={'size': 10})
    fig.suptitle('Bleaching reports from ' + year_title, fontsize=16)
    plt.show()


def generate_comparison_map(year_one_df, year_two_df, coral_map, year_title1, year_title2):

    geometry_yearone = [Point(xy)
                        for xy in zip(pd.to_numeric(year_one_df['GIS Longitude']), pd.to_numeric(year_one_df['GIS Latitude']))]

    geo_df_yearone = gpd.GeoDataFrame(
        year_one_df, crs='epsg:4326', geometry=geometry_yearone)

    geometry_yeartwo = [Point(xy)
                        for xy in zip(year_two_df['GIS Longitude'], year_two_df['GIS Latitude'])]

    geo_df_yeartwo = gpd.GeoDataFrame(
        year_two_df, crs='epsg:4326', geometry=geometry_yeartwo)

    fig, (ax1, ax2) = plt.subplots(
        ncols=2, sharex=True, sharey=True, figsize=(15, 10))

    coral_map.plot(ax=ax1, alpha=.4, color="black")
    coral_map.plot(ax=ax2, alpha=.4, color="grey")

    geo_df_yearone[geo_df_yearone['Bleaching?'] == 'YES'].plot(
        ax=ax1, markersize=20, color='green', marker='o', label='Yes')
    geo_df_yearone[geo_df_yearone['Bleaching?'] == 'NO'].plot(
        ax=ax1, markersize=20, color='red', marker='x', label='No')

    geo_df_yeartwo[geo_df_yeartwo['Bleaching?'] == 'YES'].plot(
        ax=ax2, markersize=20, color='green', marker='o', label='Yes')
    geo_df_yeartwo[geo_df_yeartwo['Bleaching?'] == 'NO'].plot(
        ax=ax2, markersize=20, color='red', marker='x', label='No')

    plt.legend(prop={'size': 10})
    fig.suptitle('Bleaching reports from left to right for years ' +
                 year_title1 + ' and ' + year_title2, fontsize=16)
    plt.show()

generate_bleach_map(df, coral_map, '2018')