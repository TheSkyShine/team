def Plotting():
    
    # Imports
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import math as m
    
    '''
    *********************************
    
    CODE FOR ELECTRICITY USAGE (RESIDENTIAL) PLOT
    
    *********************************
    '''
    
    # Takes data from CSV and uses Pandas to put into list
    file = 'Residential_Average_Monthly_kWh_and_Bills_New.csv'
    data = pd.read_csv(file, encoding='latin-1')
    
    # Converts power to temp list
    power_tempList = data["Average kWh"].tolist()
    
    # Puts the data in correct format
    date = data.Date
    date_tempList = []
    for i in date:
        a, b, c = i.split(" ")
        x,y,z = a.split("/")
        q = x + "/" + z
        date_tempList.append(q)
    
    # Takes data from 2015-2019 (Three Full Electricity Cycles) and puts into new lists
    date_list = []
    power_past = []
    k = 0
    for i in date_tempList:
        j = i[3:]
        j = int(j)
        if j > 2015:
            date_list.append(date_tempList[k])
            power_past.append(power_tempList[k])
        k += 1
    
    '''
    Sinusoidal Regression Equation From Excel for Comparison
    r^2 = 0.7228
    y = 279.2835*sin(0.5236x-2.0879) + 871.1282
    '''
    
    # Using sin equation: -a*sin(bx) + c
    # Finding a
    ymax = max(power_past)
    ymin = min(power_past)
    a = (ymax - ymin) / 2
    
    # Finding b
    # 12 is used as period due to a full power cycle taking a year
    b = (2 * m.pi) / 12
    
    # Finding c
    c = power_past[0]
    
    # Call function to get total electricty saved and incorporate into sinusoidal regression
    # Creates Regression for both old and new data
    power_regr = []
    power_change = []
    change = 90 # Called from inputs
    
    for i in range(len(power_past) + 12):
        power_regr.append(-a*m.sin((b*i)+1)+c) 
        power_change.append((-a*m.sin((b*i)+1)+c) - change)
    output_list = power_change[-13:]
    
    # Creating Plot
    
    # Updated date list
    new_dateList = []
    for i in date_list:
        new_dateList.append(i)
    
    # Future dates to be used with regression models
    future_dates = ["03/2019","04/2019","05/2019","06/2019","07/2019","08/2019","09/2019","10/2019","11/2019","12/2019","01/2020","02/2020","03/2020"]
    for i in future_dates:
        if i not in new_dateList:
            new_dateList.append(i)

    # Subplot Set-up
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(20,20))

    # Text Colors/FontSize
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['font.sans-serif'] = ['Lucida Grande']
    plt.rcParams['font.size'] = '11'
    plt.rcParams['text.color'] = 'black'

    # Window Size
    # fig = plt.figure(figsize=(12,5))
    
    # Color
    fig.patch.set_facecolor('lightcyan')
    
    # Plotting
    fig, ax = plt.subplots()
    plt.plot(date_list, power_past, label = 'Original Data')
    plt.plot(future_dates, output_list, label = 'New Data Regression')
    plt.plot(new_dateList, power_regr, label = 'Original Data Regression')
    
    # Extra Design
    axes = plt.gca()
    axes.set_ylim([400,1400])
    plt.legend(loc=2, prop={'size': 7})
    plt.title('Electricity Usage (Residential)', fontweight="bold", fontsize=16)
    plt.xlabel('Month(mm/yyyy)', fontsize=12)
    plt.xticks(rotation=80, fontsize=8)
    plt.ylabel('Energy per Month (kWh)', fontsize=12)
    plt.show()
    
    
    '''
    *********************************
    
    CODE FOR ENERGY MIX PLOT
    
    *********************************
    '''
    
    # Data
    energy_gen = 500
    austin_tot = (13.262 * 10**6) / 12 # Austin total electric energy for 2020 (MWh/y)
    energy = ['Solar', 'Gas', 'Wind', 'Coal', 'Other']
    percentage = [15, 30, 40, 10, 5]
    pv_percent = energy_gen / austin_tot
    percentage[0] += pv_percent
    percentage[3] -= pv_percent
    
    # Makes solar explode out
    solar = (0.1, 0, 0, 0, 0)
    
    # Colors
    colors = ['springgreen', 'lightcoral', 'khaki', 'aquamarine', 'thistle']
    
    # Create subplot
    plt.subplot(1,2,2)
    ax2.pie(percentage,explode = solar, colors = colors, labels = energy, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 8})
    
    # Final Parameters
    fig.patch.set_facecolor('lightcyan')
    plt.figtext(.1,1, "Energy Distribution", fontsize=15, ha='center')
    ax.axis('equal')  
    plt.tight_layout()
    plt.show()
        



