import numpy as np
import pandas as pd
import matplotlib.pyplot as plt                                                                           
import seaborn as sns

df = pd.read_csv("vgsales.csv")

df.head(5)

df.info()

"""After viewing our data and its basic information now we need to check if there are any null values."""

df.isnull().sum()

"""well we can ignoare the year and publishers because many games can be lanched from a same publisher in a same year."""

df[df.duplicated()]

"""There are no duplicates in the data.

we will create graphs for the data  in the graphs we will arreange by the game which has as the highest revenue in decending order.
"""

top_genre = df.groupby(['Genre']).sum().sort_values('NA_Sales', ascending = False)
top_genre = top_genre[['NA_Sales']].round(3)
top_genre.reset_index(inplace = True)

plt.figure(figsize = (15,5))
plt.title('Highest Revenue by Genre in North America', fontsize = 18)
plt.bar(top_genre['Genre'], top_genre['NA_Sales'], color = '#37C6AB', edgecolor = 'black', linewidth = 1)
plt.xlabel('Genre', fontsize = 15)
plt.ylabel('Revenue', fontsize = 12)
for k, v in top_genre['NA_Sales'].items():
    if v < 250:
        plt.text (k, v+30, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')
    else:
        plt.text (k, v-180, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')

top_genre = df.groupby(['Genre']).sum().sort_values('JP_Sales', ascending = False)
top_genre = top_genre[['JP_Sales']].round(3)
top_genre.reset_index(inplace = True)

plt.figure(figsize = (15,5))
plt.title('Highest Revenue by Genre in Japan', fontsize = 18)
plt.bar(top_genre['Genre'], top_genre['JP_Sales'], color = '#4CCE63', edgecolor = 'black', linewidth = 1)
plt.xlabel('Genre', fontsize = 15)
plt.ylabel('Revenue', fontsize = 12)
for k, v in top_genre['JP_Sales'].items():
    if v > 300:
        plt.text (k, v-80, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')
    else:
        plt.text (k, v+20, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')

top_genre = df.groupby(['Genre']).sum().sort_values('EU_Sales', ascending = False)
top_genre = top_genre[['EU_Sales']].round(3)
top_genre.reset_index(inplace = True)

plt.figure(figsize = (15,5))
plt.title('Highest Revenue by Genre in Europian Union', fontsize = 18)
plt.bar(top_genre['Genre'], top_genre['EU_Sales'], color = '#0A86D9', edgecolor = 'black', linewidth = 1)
plt.xlabel('Genre', fontsize = 15)
plt.ylabel('Revenue', fontsize = 12)
for k, v in top_genre['EU_Sales'].items():
    if v > 300:
        plt.text (k, v-80, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')
    else:
        plt.text (k, v+20, '$' + str(v), fontsize = 12, rotation = 90, color = 'black', ha = 'center')

"""By the help of these three graphs we can find the most genre solds in the EU, JP and NA. In japan most people play role playing genre games rather than action games."""
