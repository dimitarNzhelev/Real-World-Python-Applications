import pandas

info = pandas.read_csv("Cities.txt")

name = list(info["NAME"])
lat = list(info["LAT"])
lon = list(info["LON"])

info = {}
br = 0

for city in name:
    info[city] = [float(lat[br]),float(lon[br])]
    br += 1
    