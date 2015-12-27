#!/usr/bin/python
import csv
import time
import matplotlib.pyplot as plt

input_file = "./seattle_incidents_summer_2014.csv"

time_data = list()
type_data = list()
with open(input_file, 'rb') as csvfile:
    csvcontent = csv.reader(csvfile, delimiter=",")
    begin = True
    for row in csvcontent:
        if begin:
            begin = False
            colmap = {
                'Offense Type': row.index("Offense Type"),
                'Summarized Offense Description': row.index("Summarized Offense Description"),
                'Occurred Date or Date Range Start': row.index("Occurred Date or Date Range Start")
            }
        else:
            mytime = time.strptime(row[colmap['Occurred Date or Date Range Start']], '%m/%d/%Y %I:%M:%S %p')
            mytype = row[colmap['Summarized Offense Description']]
            time_data.append(mytime)
            type_data.append(mytype)
    x = range(24)
    y = list()
    y_dict = {}
    for mytime in time_data:
        h = int(time.strftime('%H', mytime))
        if h in y_dict:
            y_dict[h] += 1
        else:
            y_dict[h] = 1
    for var in x:
        y.append(y_dict[var])
    plt.bar(x,y)
    plt.xlim(0, 24)
    plt.xticks(range(25))
    plt.xlabel('Hour of the day')
    plt.ylabel('Total number of incidents')
    plt.show()
