import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Text Colors
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['font.sans-serif'] = ['Lucida Grande']
plt.rcParams['font.size'] = '11'
plt.rcParams['text.color'] = 'black'

# Data
energy = ['Solar', 'Gas', 'Electric', 'Coal']
percentage = [15, 30, 45, 10]

# Makes solar explode out
solar = (0.1, 0, 0, 0)

# Colors
colors = ['springgreen', 'lightcoral', 'khaki', 'aquamarine']

# Create subplot
fig, ax = plt.subplots()
ax.pie(percentage, explode = solar, colors = colors, labels = energy, autopct='%1.1f%%', shadow=True, startangle=90)

# Final Parameters
fig.patch.set_facecolor('lightcyan')
plt.figtext(.1,1, "Energy Distribution", fontsize=15, ha='center')
ax.axis('equal')  
plt.tight_layout()
plt.show()
