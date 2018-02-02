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