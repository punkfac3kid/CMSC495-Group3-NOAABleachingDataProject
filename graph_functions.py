import pandas as pd
import matplotlib.pyplot as plt
#from get_data_file import BIG_DATA

def __combined_data_percent(BIG_DATA):
    """
    Creates a combined DataFrame of 2014 and 2015 % bleached
    """
    #The number columns will be equal to the number of unique values in the YEAR column of BIG_DATA
    #The name will be the values
    df_combo = pd.DataFrame(columns=BIG_DATA['YEAR'].unique(),
                            index=['0%', '1-10%', '11-30%', '31-50%', '51-75%', '76-100%'])

    #Goes through BIG_DATA to pull out desired values that match the year and % bleached to create a subset dataframe
    #Counts the rows of the subset dataframe and sets that value to the corelating spot within the df_combo dataframe
    for col in df_combo:
        df_combo.at['0%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '0%')
                                                 & (BIG_DATA['YEAR'] == col)])
        df_combo.at['1-10%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '1-10%')
                                                    & (BIG_DATA['YEAR'] == col)])
        df_combo.at['11-30%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '11-30%')
                                                     & (BIG_DATA['YEAR'] == col)])
        df_combo.at['31-50%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '31-50%')
                                                     & (BIG_DATA['YEAR'] == col)])
        df_combo.at['51-75%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '51-75%')
                                                     & (BIG_DATA['YEAR'] == col)])
        df_combo.at['76-100%', col] = len(BIG_DATA[(BIG_DATA['% BLEACHED'].str.strip() == '76-100%')
                                                      & (BIG_DATA['YEAR'] == col)])
    return df_combo

def __combined_data_severity(BIG_DATA):
    """
    Creates a combined DataFrame for 2014 and 2015 Severity
    """
    df_combo = pd.DataFrame(columns=BIG_DATA['YEAR'].unique(),
                            index=['None', 'Paling', 'Partial Bleaching', 'Upper Surface', 'Bleaching'])

    #Similar to the method used in __combined_data_percent(); however forced the strings to be read as lowercase
    #and stripped excess spaces to have uniformity in the data
    for col in df_combo:
        df_combo.at['None', col] = len(BIG_DATA[((BIG_DATA['SEVERITY'].str.lower()).str.strip() == 'none')
                                                   & (BIG_DATA['YEAR'] == col)])
        df_combo.at['Paling', col] = len(BIG_DATA[((BIG_DATA['SEVERITY'].str.lower()).str.strip() == 'paling')
                                                     & (BIG_DATA['YEAR'] == col)])
        df_combo.at['Partial Bleaching', col] = len(BIG_DATA[((BIG_DATA['SEVERITY'].str.lower()).str.strip() ==
                                                                 'partial bleaching') & (BIG_DATA['YEAR'] == col)])
        df_combo.at['Upper Surface', col] = len(BIG_DATA[((BIG_DATA['SEVERITY'].str.lower()).str.strip() ==
                                                             'upper surface') & (BIG_DATA['YEAR'] == col)])
        df_combo.at['Bleaching', col] = len(BIG_DATA[((BIG_DATA['SEVERITY'].str.lower()).str.strip() ==
                                                         'bleaching') & (BIG_DATA['YEAR'] == col)])
    return df_combo

def __line_graph_data(BIG_DATA):
    """
    CURRENTLY FIXING
    Creates a DataFrame to be used by the Temperature Line graph
    """
    df_temp = pd.DataFrame(columns=['index', BIG_DATA['YEAR'].unique()])
    for col in df_temp:
        df_sep = BIG_DATA[BIG_DATA['YEAR'] == col]
        df_sep = df_sep[df_sep['BOTTOM_TEMP(F)'] != 'no data']
        df_temp[col] = df_sep['BOTTOM_TEMP(F)']
    return df_temp

def bar_bleach(BIG_DATA):
    """
    Every years percent categories must be tallied
    Will have a multi-bar graph of each year outputting the tallied categories
    Index: Percent Categories (6 Categories)
    Columns: Years
    Values: tallied values
    Create new data frame in this format?
    """
    df_combo = __combined_data_percent(BIG_DATA)
    df_combo.plot(kind='bar', figsize=(15, 8))
    plt.xlabel('Percent Bleach Category')
    plt.ylabel('Amount in Each Category')
    plt.title('Comparison of Percent Bleached by Year ')
    plt.show()

def pie_bleach(BIG_DATA):
    """
    Creates pie chart for every year within the combined dataframe
    Handles the percent bleaching data
    """
    df_combo = __combined_data_percent(BIG_DATA)
    df_combo.groupby(df_combo.index).sum().plot(kind='pie', subplots=True, figsize=(20, 8), autopct='%1.0f%%',
                                                title='Percent Bleached')
    plt.show()

def bar_severity(BIG_DATA):
    """
    Creates a multi-bar graph for every year
    Handles the bleaching severity data
    """
    df_combo = __combined_data_severity(BIG_DATA)
    df_combo.plot(kind='bar', figsize=(15, 10))
    plt.xlabel('Bleach Severity Category')
    plt.ylabel('Amount in Each Category')
    plt.title('Comparison of Severity by Year ')
    plt.show()

def pie_severity(BIG_DATA):
    """
    Creates a pie graph for every year
    Handles the bleaching severity data
    """
    df_combo = __combined_data_severity(BIG_DATA)
    df_combo.groupby(df_combo.index).sum().plot(kind='pie', subplots=True, figsize=(20, 8), autopct='%1.0f%%',
                                                title='Bleach Severity')
    plt.show()

def line_graph(BIG_DATA):
    """
    CURRENTLY FIXING
    Creates a line graph for every year
    """
    df_temp = __line_graph_data(BIG_DATA)
    df_temp.plot(kind='line', x='index')

#implement a line graph of temperature over time
#df_sep = BIG_DATA[BIG_DATA['YEAR'] == '2014']
#df_temp = df_sep[df_sep['BOTTOM_TEMP(F)'] != 'no data']
#print(line_graph())