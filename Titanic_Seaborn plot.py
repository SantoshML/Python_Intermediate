# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 00:35:37 2018

@author: Santosh Kumar
"""

##---------------------Titanic---------------------------------###

#Seaborn Plot

import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv("train.csv")
titanic = titanic.loc[:,["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic = titanic.dropna()

import seaborn as sns

#Histogram/Distribution plot
sns.distplot(titanic["Age"])
plt.show()


#Kernel density plot

sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")

## Type of styles in seaborn

sns.set_style("white")
sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")
sns.despine(left = True,bottom = True)

#How to subset a datframe for plotting

g = sns.FacetGrid(titanic,col = "Pclass",size = 6)
g.map(sns.kdeplot,"Age",shade = True)
sns.despine(left = True,bottom = True)

#Adding one more condition for subset row
g = sns.FacetGrid(titanic, col="Survived", row="Embarked")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

#Purpose of hue
g = sns.FacetGrid(titanic,col = "Survived",row = "Pclass",hue = "Sex",size = 3)
g.map(sns.kdeplot,"Age",shade = True)
sns.despine(left = True,bottom = True)
plt.show()

#How to add legend to hue
g = sns.FacetGrid(titanic,col = "Survived",row = "Pclass",hue = "Sex",size = 3)
g=(g.map(sns.kdeplot,"Age",shade = True).add_legend())
sns.despine(left = True,bottom = True)
plt.show()


