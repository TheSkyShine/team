import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as m

# Takes data from CSV and uses Pandas to put into list
file = 'Residential_Average_Monthly_kWh_and_Bills.csv'
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

# Takes data from 2015 and on and puts into new lists
date_list = []
power_list = []
k = 0
for i in date_tempList:
    j = i[3:]
    j = int(j)
    if j > 2015:
        date_list.append(date_tempList[k])
        power_list.append(power_tempList[k])
    k += 1

# Sinusoidal Regression Equation
# r^2 = 0.7228
# y = 279.2835*sin(0.5236x-2.0879) + 871.1282

# Using sin equation -a*sin(bx) + c
# Finding a
ymax = max(power_list)
ymin = min(power_list)
a = (ymax - ymin) / 2

# Finding b
# 12 is used as period due to a full power cycle taking a year
b = (2 * m.pi) / 12

# Finding c
c = power_list[0]

# Creating y values with regression equation
power_newList = []
for i in range(len(power_list)):
    power_newList.append(-a*m.sin(b*i)+c)

# Creating Plot

# Sort by indexes
x_indexes = len(date_list)

# Plotting

# Color
fig = plt.figure()
fig.patch.set_facecolor('lightcyan')

# Plotting Figures
plt.plot(date_list, power_list, label = 'Original Data')
plt.plot(date_list, power_newList, label = 'Updated Data')

# Extra Design
plt.legend(loc=1, prop={'size': 5})
plt.title('Electricity Usage', fontweight="bold")
plt.xlabel('Date')
plt.xticks(rotation=80, fontsize=7)
plt.ylabel('Power (kWh)')
plt.show()



