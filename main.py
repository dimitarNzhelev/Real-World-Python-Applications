import folium
import random
from data import info

colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'pink', 'lightblue', 'lightgreen','gray', 'black', 'lightgray']

map = folium.Map(location= info["Stara Zagora"], zoom_start=7, tiles = "Stamen Terrain")

for key,value in info.items():
    map.add_child(folium.CircleMarker(location= value, popup=f"This is {key}", fill = True, radius=10, color = 'white', fill_opacity = 0.7,fill_color = random.choice(colors)))

map.save("mapSofia.html")