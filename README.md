# Python_Intermediate
import csv
f = open("guns.csv","r")
f_read = csv.reader(f)
data = list(f_read)
print(data[0:5])
header = data[0]
data = data[1:]
print(header)
print(data[0:5])
years = [each[1] for each in data]
year_counts = {}

for each in years:
    if each in year_counts:
        year_counts[each] +=1
    else:
        year_counts[each] = 1 
print(year_counts)
import datetime
dates = []

for each in data:
    yrs = int(each[1])
    mnth = int(each[2])
    dat = datetime.datetime(year = yrs,month = mnth,day = 1)
    dates.append(dat)
print(dates[0:5])
date_counts = {}

for each in dates:
    if each in date_counts:
        date_counts[each] +=1
    else:
        date_counts[each] = 1

print(date_counts)
sex = [each[5] for each in data]

sex_counts = {}

for each in sex:
    if each in sex_counts:
        sex_counts[each] +=1
    else:
        sex_counts[each] = 1
        
race = [each[7] for each in data]

race_counts = {}

for each in race:
    if each in race_counts:
        race_counts[each] +=1
    else:
        race_counts[each] = 1
print(race_counts)
print()
    
f = open("census.csv","r")
f_read = csv.reader(f)
census = list(f_read)
print(census)
mapping = {"Asian/Pacific Islander":15834141,"Black":40250635,"Native American/Native Alaskan":3739506,"Hispanic":44618105,"White":197318956}
race_per_hundredk = {}
for each in race_counts:
    race_per_hundredk[each] = (race_counts[each]/mapping[each])*100000
    
print(race_per_hundredk)
intents = [each[3] for each in data]
races = [each[7] for each in data]

homicide_race_counts = {}
for i,race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] +=1
        else:
            homicide_race_counts[race] = 1

#homicide_race_counts[each] = {((homicide_race_counts[each]/mapping[each])*100000) 

for each in homicide_race_counts:
    homicide_race_counts[each] = (homicide_race_counts[each]/mapping[each])*100000                          

