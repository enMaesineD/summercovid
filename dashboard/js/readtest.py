#
# readtest.py - reads a csv file and writes out a .js file suitable for use in js scripts
# Step 1 - download latest csv
# John Hopkins University COVID data
# https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/06-11-2020.csv
# Step 2 - view in spreadsheet program and change countries or states with a ","
# Bonaire, Sint Eustatius and Saba (also Korea, South - 
# Bonaire Sint Eustatius and Saba
# Step3 - run script
# 
fi = open("06-11-2020.csv","r")
delfirst = fi.readline() # skip over titles
lines = fi.readlines()
fi.close()

conflist = []
for line in lines:
    templist = line.split(",")
    pname = templist[2]
    cname = templist[3]
    date = templist[4]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    conflist.append({"pname":pname,"cname":cname,"confirmed":conf, "lat":lat, "lon": lon})

conflist.sort(key=lambda s: s['confirmed'], reverse=True)
fo = open("06-11-2020.js","w")
fo.write("data = " + str(conflist))
fo.close()
