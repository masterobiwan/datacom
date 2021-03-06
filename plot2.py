#!/usr/bin/python
import csv
import time
import matplotlib.pyplot as plt

input_file = "./seattle_incidents_summer_2014.csv"

selected_hours = range(12, 24)
selected_hours.append(0)
data_dict = {}
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
            myhour = int(time.strftime('%H', mytime))
            if myhour in selected_hours:
                if mytype in data_dict:
                    data_dict[mytype] += 1
                else:
                    data_dict[mytype] = 1
    plot_dict = {}
    n = 0
    for key, value in sorted(data_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        n += 1
        if n <= 5:
            plot_dict[key] = value
    colors = ['lightgreen', 'coral', 'lightskyblue', 'lightpink', 'tan']
    plt.pie(plot_dict.values(), labels=plot_dict.keys(), colors=colors, autopct='%i')
    plt.show()
