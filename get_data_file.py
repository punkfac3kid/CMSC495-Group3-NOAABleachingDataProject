"""
get_data_file.py

This program was written by Zack Mason on 11/1/2021.
This application creates a series of GUI windows that
allow the user to download and subset Florida keys
bleachwatch data by year. It also allows the user to
choose which kind of visualization option they would
like to pursue with their custom dataset. Finally,
This program also standardizes the data between years
so that the datasets are interoperable.
"""
import urllib.request
#from tkinter import *
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import Button
import tkinter as tk
import os
import sys
#from pandas.io.feather_format import read_feather
#import requests
import pandas as pd
from pandas_ods_reader import read_ods

BIG_DATA = pd.DataFrame()

data_dictionary = {
"https://www.nodc.noaa.gov/archive/arc0073/0126654/2.2/data/1-data/Copy%20of%20BW_2014_Data_MML.csv":
"bleach_watch_2014.csv",
"https://www.nodc.noaa.gov/archive/arc0084/0140822/2.2/data/1-data/BW_2015_Data_MML.csv":
"bleach_watch_2015.csv",
"https://www.nodc.noaa.gov/archive/arc0100/0157068/1.1/data/1-data/BW_2016_Data_MML-2016.csv":
"bleach_watch_2016.csv",
"https://www.nodc.noaa.gov/archive/arc0115/0168768/1.1/data/1-data/BW_2017_Data_MML-2017.csv":
"bleach_watch_2017.csv",
"https://www.nodc.noaa.gov/archive/arc0150/0206104/1.1/data/1-data/BW_2018_Data_MML.ods":
"bleach_watch_2018.csv",
"https://www.nodc.noaa.gov/archive/arc0158/0213521/1.1/data/1-data/BW_2019_Data_MML.ods":
"bleach_watch_2019.csv",
"https://www.nodc.noaa.gov/archive/arc0164/0221973/1.1/data/1-data/BW_2020_Data_MML.ods":
"bleach_watch_2020.csv"}


def standardize_data(d_f):
    """
    This module standardizes each individual data file so that
    all of the data are interoperable.

    d_f - incoming data frame for each data file selected by the user.

    column_dict: dictionary. Lists headers found in the original data
    as the keys and then the standard version of the header as the
    value. This is used to replace the column headers later on.

    column_list: list. This is a list of the column names found in
    the incoming d_f.
    """
    #print("Standardizing data file")
    d_f.drop(d_f.columns[d_f.columns.str.contains('unnamed',case = False)],
    axis = 1, inplace = True)
    d_f.drop(d_f.columns[d_f.columns.str.contains('Baseline Indicator',case = False)],
    axis = 1, inplace = True)

    column_dict = {"SST": "SST(F)", "BOTTOM TEMP": "BOTTOM_TEMP(F)", "AIR TEMP": "AIR_TEMP(F)",
    "WIND": "WIND_SPEED(KNOTS)", "MIN DEPTH": "MIN_DEPTH(FT)", "MAX DEPTH": "MAX_DEPTH(FT)"}

    d_f = d_f.rename(columns=str.upper)
    d_f = d_f.rename(columns=str.strip)
    #column_list = []
    column_list = d_f.columns
    for header in column_list:
        for key in column_dict:
            if key in header:
                print("Found " + key)
                real_header = column_dict.get(key)
                print("New Header: " + real_header)
                d_f = d_f.rename(columns = {header: real_header})
    d_f.dropna(subset = ["DATE"], inplace=True)
    return d_f

def data_frame_conversion(file_list):
    """
    This module accepts a list of files as input. It then
    iterates over that list to convert each file into a
    pandas data frame. Some of these files are in the .csv
    file format and others are not. However, the extension
    of the file can't be used as for some reason there is a
    bug with the open document spreadsheet files. If they are
    saved as ods files python has trouble converting them into
    data frames. However, when they are saved as csv files but
    read like ods files, python has no issues.

    This module also uses the BIG_DATA global variable. This is
    done for ease of access. The file referenced in BIG_DATA will
    need to be accessible by multiple graphing functions.

    This module also calls the standardize_data module to edit
    the data frames that are produced here. It then appends the
    standardized data to the BIG_DATA file.
    """
    global BIG_DATA
    BIG_DATA = pd.DataFrame()
    for file_name in file_list:
        #print("Loading the following file: " + str(file_name))

        try:
            #print("TRYING CSV")
            d_f = pd.read_csv(file_name)
        except pd.errors.ParserError:
            try:
                #print("TRYING ODS")
                d_f = read_ods(file_name)
            except pd.errors.ParserError:
                #print("TRYING EXCEL/ODF")
                d_f = pd.read_excel(file_name, engine="odf")

        standard_d_f = standardize_data(d_f)
        del d_f
        BIG_DATA = BIG_DATA.append(standard_d_f, ignore_index=False)
        del standard_d_f
    print(BIG_DATA)


def get_keys(dictionary):
    """
    This function gets all the keys from an input dictionary and returns them as a list.
    """
    key_list = []
    for key in dictionary.keys():
        key_list.append(key)
    #print(str(key_list))
    return key_list

def get_values(dictionary):
    """
    This function gets all the values from an input dictionary and returns them as a list.
    """
    value_list = []
    for value in dictionary.values():
        value_list.append(value)
    #print(str(value_list))
    return value_list


def second_gui():
    """
    This method builds another GUI. This GUI asks the user which type of
    graph they would like to produce.
    """

    def new_display_selected(new_choice):
        """
        This module just prints to the screen the user's selection whenever
        a new option is chosen.
        """
        new_choice = options.get()
        print(new_choice + " selected")

    def visualize():
        """
        This is where the graphing function calls will go. This is called when the user hits
        "submit" in the second GUI. There should be some if, elif statements here to make
        sure that the correct graphing function is called as well.
        """
        my_selection = options.get()
        print("Running the " + str(my_selection) + " visualization function!")
        window.destroy()

    window = tk.Tk()
    window.title("Data Visualization Tool")
    window.geometry("400x125")
    window.eval('tk::PlaceWindow . center')
    frame1 = tk.Frame(master=window)
    #, width=200, height=100)
    frame1.pack()

    frame2 = tk.Frame(master=window)
    #, width=200, height=100)
    frame2.pack()

    greeting = tk.Label(master=frame1, text="How would you like to visualize these data?")
    greeting.pack(padx=5, pady=5)

    label_one = tk.Label(master=frame1, text="Choose a graph option:    ")
    label_one.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    options = tk.StringVar(window)
    options.set("Select Graph Type") # default value
    om1 =tk.OptionMenu(frame1, options, "Line Plot","Bar Graph", "Pie Chart",
    command=new_display_selected)

    om1.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)

    button = Button(frame2,
	text = 'Submit',
	command = visualize)
    button.pack(padx=5, pady=5)

    window.mainloop()


def get_data(dictionary):
    """
    This function gets the data requested by the user and downloads it to the user's
    current working directory. It is called from the button click in the setup gui.
    """

    print("Loading Data...")
    directory = os.getcwd()
    i = 0
    filename_list = get_values(dictionary)
    url_list = get_keys(dictionary)
    for my_filename in filename_list:
        my_url = url_list[i]
        #print("URL listed as: " + str(my_url))
        file_path = directory + "\\" + my_filename
        #print("Grabbing file and saving it here: " + file_path)
        try:
            urllib.request.urlretrieve(my_url, file_path)
        except FileNotFoundError:
            print("Couldn't retrieve file " + my_filename + " \nfrom: " + str(my_url))
            sys.exit()
        i += 1

def setup():
    """
    Initial GUI Construction Below.

    """

    def button_click():
        """
        This function checks the checkboxes to see which are actually checked. Then it goes
        through and cpncatenates the data for each selected year to a data frame.
        """
        data_list = []
        my_prefix = os.getcwd()
        if check_var1.get() == 1:
            #print("2014 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2014.csv"
            data_list.append(file_path)
        if check_var2.get() == 1:
            #print("2015 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2015.csv"
            data_list.append(file_path)
        if check_var3.get() == 1:
            #print("2016 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2016.csv"
            data_list.append(file_path)
        if check_var4.get() == 1:
            #print("2017 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2017.csv"
            data_list.append(file_path)
        if check_var5.get() == 1:
            #print("2018 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2018.csv"
            data_list.append(file_path)
        if check_var6.get() == 1:
            #print("2019 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2019.csv"
            data_list.append(file_path)
        if check_var7.get() == 1:
            #print("2020 Checked")
            file_path = my_prefix + "\\" + "bleach_watch_2020.csv"
            data_list.append(file_path)

        #print(str(data_list))
        data_frame_conversion(data_list)
        window.destroy()

    window = tk.Tk()
    window.title("Bleach Watch Data Visualization Tool")
    #window.geometry("350x200")
    window.eval('tk::PlaceWindow . center')
    frame0 = tk.Frame(master=window)
    #, width=200, height=100, borderwidth=5)
    frame0.grid()
    label_one = tk.Label(master=frame0, text="Which years of data would you like to visualize?")
    label_one.grid(sticky=tk.NS)
    frame1 = tk.Frame(master=window)
    frame1.grid()
    frame2 = tk.Frame(master=window)
    #, width=200, height=100)
    frame2.grid()
    #button = tk.Button(
    #    master=frame2,
    #    text="Submit"
    #)
    #button.grid(padx=5, pady=5, sticky=tk.EW)
    #button.bind('<Button-1>', button_click)

    button = Button(frame2,
	text = 'Submit',
	command = button_click)
    button.grid(padx=5, pady=5, sticky=tk.EW)

    check_var1 = IntVar()
    check_var2 = IntVar()
    check_var3 = IntVar()
    check_var4 = IntVar()
    check_var5 = IntVar()
    check_var6 = IntVar()
    check_var7 = IntVar()
    c_1 = Checkbutton(frame1, text = "2014", variable = check_var1, onvalue = 1,
    offvalue = 0, height=3, width = 5)
    c_2 = Checkbutton(frame1, text = "2015", variable = check_var2, onvalue = 1,
    offvalue = 0, height=3, width = 5)
    c_3 = Checkbutton(frame1, text = "2016", variable = check_var3, onvalue = 1,
    offvalue = 0, height=3, width = 5)
    c_4 = Checkbutton(frame1, text = "2017", variable = check_var4, onvalue = 1,
    offvalue = 0, height=3, width = 5)
    c_5 = Checkbutton(frame1, text = "2018", variable = check_var5, onvalue = 1,
    offvalue = 0, height=3, width = 5)
    c_6 = Checkbutton(frame1, text = "2019", variable = check_var6,
    onvalue = 1, offvalue = 0, height=3, width = 5)
    c_7 = Checkbutton(frame1, text = "2020", variable = check_var7,
    onvalue = 1, offvalue = 0, height=3, width = 5)
    c_1.grid(row = 0, column = 0)
    c_2.grid(row = 0, column = 1)
    c_3.grid(row = 0, column = 2)
    c_4.grid(row = 0, column = 3)
    c_5.grid(row = 1, column = 0)
    c_6.grid(row = 1, column = 1)
    c_7.grid(row = 1, column = 2)

    window.mainloop()

# Main Block Below

get_data(data_dictionary)
setup()
second_gui()

prefix = os.getcwd()
final_file_path = prefix + "\\" + "test.csv"
BIG_DATA.to_csv(final_file_path, index=False)
