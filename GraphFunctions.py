import pandas as pd
import matplotlib.pyplot as plt
"""
NEED TO MAKE FILE INTO A CLASS
"""

'''function to get data for testing provides 2014 and 2015'''
def get_2014():
    # Importing test file using Copy of 2014 Data
    excel_df_2014 = pd.read_csv("Copy of BW_2014_Data_MML.csv", encoding='windows-1252')
    excel_df_2014 = excel_df_2014.drop(['Contact Method', 'Name', 'Date', 'Time', 'City', 'State', 'Observer', 'Vessel',
                                        'Depth (ft)', 'Location', 'Region/Buoy#', 'Reef Zone', 'Wind Spd.',
                                        'Cloud Cover',
                                        'Branching/Pillar', 'Brain', 'Encrusting/Mound/Boulder', 'Flowering/Cup',
                                        'Leaf/Plate/Sheet', 'Fleshy',
                                        'Max Depth', 'Min Depth', 'Baseline Indicators', 'Baseline Indicators.1',
                                        'Baseline Indicators.2',
                                        'Notes'], axis=1)
    return excel_df_2014

def get_2015():
    # Importing test file using 2015 Data
    excel_df_2015 = pd.read_csv("BW_2015_Data_MML.csv", encoding='windows-1252')
    excel_df_2015 = excel_df_2015.drop(['Contact Method', 'Name', 'Date', 'Time', 'City', 'State', 'Observer', 'Vessel',
                                        'Depth (ft)', 'Location', 'Region/Buoy#', 'Reef Zone', 'Wind Spd.',
                                        'Cloud Cover',
                                        'Branching/Pillar', 'Brain', 'Encrusting/Mound/Boulder', 'Flowering/Cup',
                                        'Leaf/Plate/Sheet', 'Fleshy',
                                        'Max Depth (ft)', 'Min Depth (ft)', 'Baseline Indicators',
                                        'Baseline Indicators.1', 'Baseline Indicators.2',
                                        'Notes'], axis=1)
    return excel_df_2015

'''Creates a combined DataFrame of 2014 and 2015 % bleached'''
def combined_data_percent():
    df_2014 = get_2014()
    df_2015 = get_2015()
    combo_dict = [[0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0]]
    df_combo = pd.DataFrame(combo_dict, columns=['2014', '2015'],
                            index=['0%', '1-10%', '11-30%', '31-50%', '51-75%', '76-100%'])

    '''Increases the cell value in the data frame by one when str matches'''
    for col in df_2014['% bleached']:
        if col == '0%':
            df_combo.at['0%', '2014'] = df_combo.at['0%', '2014'] + 1
        elif col == '1-10%':
            df_combo.at['1-10%', '2014'] = df_combo.at['1-10%', '2014'] + 1
        elif col == '11-30%':
            df_combo.at['11-30%', '2014'] = df_combo.at['11-30%', '2014'] + 1
        elif col == '31-50%':
            df_combo.at['31-50%', '2014'] = df_combo.at['31-50%', '2014'] + 1
        elif col == '51-75%':
            df_combo.at['51-75%', '2014'] = df_combo.at['51-75%', '2014'] + 1
        elif col == '76-100%':
            df_combo.at['76-100%', '2014'] = df_combo.at['76-100%', '2014'] + 1

    '''Increases the cell value in the data frame by one when str matches'''
    for col in df_2015['% bleached']:
        if col == '0%':
            df_combo.at['0%', '2015'] = df_combo.at['0%', '2015'] + 1
        elif col == '1-10%':
            df_combo.at['1-10%', '2015'] = df_combo.at['1-10%', '2015'] + 1
        elif col == '11-30%':
            df_combo.at['11-30%', '2015'] = df_combo.at['11-30%', '2015'] + 1
        elif col == '31-50%':
            df_combo.at['31-50%', '2015'] = df_combo.at['31-50%', '2015'] + 1
        elif col == '51-75%':
            df_combo.at['51-75%', '2015'] = df_combo.at['51-75%', '2015'] + 1
        elif col == '76-100%':
            df_combo.at['76-100%', '2015'] = df_combo.at['76-100%', '2015'] + 1
    
    return df_combo

'''Creates a combined DataFrame for 2014 and 2015 Severity'''
def combined_data_severity():
    df_2014 = get_2014()
    df_2015 = get_2015()
    combo_dict = [[0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0]]
    df_combo = pd.DataFrame(combo_dict, columns=['2014', '2015'],
                            index=['None', 'Paling', 'Partial Bleaching', 'Upper Surface', 'Bleaching'])

    '''Increases the cell value in the data frame by one when str matches'''
    for col in df_2014['Severity']:
        if col == 'none' or col == 'None':
            df_combo.at['None', '2014'] = df_combo.at['None', '2014'] + 1
        elif col == 'Paling' or col == 'paling':
            df_combo.at['Paling', '2014'] = df_combo.at['Paling', '2014'] + 1
        elif col == 'Partial bleaching' or col == 'partial bleaching':
            df_combo.at['Partial Bleaching', '2014'] = df_combo.at['Partial Bleaching', '2014'] + 1
        elif col == 'Upper surface' or col == 'upper surface':
            df_combo.at['Upper Surface', '2014'] = df_combo.at['Upper Surface', '2014'] + 1
        elif col == 'Bleaching' or col == 'bleaching':
            df_combo.at['Bleaching', '2014'] = df_combo.at['Bleaching', '2014'] + 1

    '''Increases the cell value in the data frame by one when str matches'''
    for col in df_2015['Severity']:
        if col == 'none' or col == 'None':
            df_combo.at['None', '2015'] = df_combo.at['None', '2015'] + 1
        elif col == 'Paling' or col == 'paling':
            df_combo.at['Paling', '2015'] = df_combo.at['Paling', '2015'] + 1
        elif col == 'Partial bleaching' or col == 'partial bleaching':
            df_combo.at['Partial Bleaching', '2015'] = df_combo.at['Partial Bleaching', '2015'] + 1
        elif col == 'Upper surface' or col == 'upper surface':
            df_combo.at['Upper Surface', '2015'] = df_combo.at['Upper Surface', '2015'] + 1
        elif col == 'Bleaching' or col == 'bleaching':
            df_combo.at['Bleaching', '2015'] = df_combo.at['Bleaching', '2015'] + 1

    return df_combo

"""
Every years percent categories must be tallied
Will have a multi-bar graph of each year outputting the tallied categories
Index: Percent Categories (6 Categories)
Columns: Years 
Values: tallied values
Create new data frame in this format?
"""
def bar_bleach():
    df_combo = combined_data_percent()
    df_combo.plot(kind='bar', figsize=(15,8))
    plt.xlabel('Percent Bleach Category')
    plt.ylabel('Amount in Each Category')
    plt.title('Comparison of Percent Bleached by Year ')
    plt.show()

'''Creates pie chart for every year within the combined dataframe'''
def pie_bleach():
    df_combo = combined_data_percent()
    df_combo.groupby(df_combo.index).sum().plot(kind='pie', subplots=True, figsize=(20,8), autopct='%1.0f%%',
                                                title='Percent Bleached')
    plt.show()

def bar_severity():
    df_combo = combined_data_severity()
    df_combo.plot(kind='bar', figsize=(15, 10))
    plt.xlabel('Bleach Severity Category')
    plt.ylabel('Amount in Each Category')
    plt.title('Comparison of Severity by Year ')
    plt.show()

def pie_severity():
    df_combo = combined_data_severity()
    df_combo.groupby(df_combo.index).sum().plot(kind='pie', subplots=True, figsize=(20, 8), autopct='%1.0f%%',
                                                title='Bleach Severity')
    plt.show()

"""Still want to create a line graph of temperature over time"""