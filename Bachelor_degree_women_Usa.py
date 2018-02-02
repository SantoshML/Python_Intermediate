# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:11:21 2018

@author: Santosh Kumar
"""



######------------percent-bachelors-degrees-women-usa--------#####
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees["Year"],women_degrees["Biology"])
plt.show()


plt.plot(women_degrees["Year"],women_degrees["Biology"],c ='b',label = "Women")
plt.plot(women_degrees["Year"],(100-np.array(women_degrees["Biology"])),c = 'g',label = "Men")
plt.legend(loc = "upper right")
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.show()


fig,ax = plt.subplots()
ax.plot(women_degrees["Year"],women_degrees["Biology"],c = 'b',label = 'Women')
ax.plot(women_degrees["Year"],(100-np.array(women_degrees["Biology"])),c = 'g',label = 'Men')
ax.tick_params(bottom = "off",top = "off",left = "off",right = "off")
ax.set_title("Percentage of Biology Degrees Awarded By Gender")
ax.legend(loc = "upper right")
plt.show()



major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.tick_params(bottom ='off',top = 'off',left = 'off',right = 'off')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_title(major_cats[sp])
# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()
