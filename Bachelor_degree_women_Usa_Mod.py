# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:41:50 2018

@author: Santosh Kumar
"""
--------## Visualization_STEM_USA_DATASET##---------------------- ##-----------------------------------


fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if sp == 0:
        ax.text(2005,87,"Men")
        ax.text(2002,8,"Women")
    elif sp == 5:    
        ax.text(2005,62,"Men")
        ax.text(2001,35,"Women")
        
    
#plt.legend(loc='upper right')
plt.show()

##Generating Graph for All the Branch

import os
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(16,20))

##Generating First column of the plot

for sp in range(0,18,3):
    corr_plot = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[corr_plot]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[corr_plot]], c=cb_orange, label='Men', linewidth=3)
    for key,spines in ax.spines.items():
        spines.set_visible(False)
        
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[corr_plot])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if corr_plot == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif corr_plot == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')

##Generating Second column of the plot

for sp in range(1,16,3):
    ax = fig.add_subplot(6,3,sp+1)
    corr_plot = int((sp-1)/3)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[corr_plot]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[corr_plot]], c=cb_orange, label='Men', linewidth=3)
    for key,spines in ax.spines.items():
        spines.set_visible(False)
        
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[corr_plot])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if corr_plot == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
##Generating the third Column        
for sp in range(2,20,3):
    corr_plot =int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[corr_plot]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[corr_plot]], c=cb_orange, label='Men', linewidth=3)
    for key,spines in ax.spines.items():
        spines.set_visible(False)
        
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[corr_plot])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if corr_plot == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif corr_plot == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
    
plt.show()