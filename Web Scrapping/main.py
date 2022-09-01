import requests
from bs4 import BeautifulSoup
import pandas

l = []
base_url = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="

for page in range(0,30,10):
    print((base_url+str(page)))
    r = requests.get(base_url+str(page))
    c =r.content
    soup = BeautifulSoup(c,"html.parser")

    all = soup.find_all("div", {"class":"propertyRow"})

    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class": "propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span",{"class": "propAddressCollapse"})[1].text
        d["Price"]=item.find("h4", {"class": "propPrice"}).text.replace("\n","").replace(" ","")

        try:
            d["Beds"]=item.find("span",{"class": "infoBed"}).find("b").text
        except:
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class": "infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["FullBaths"]=item.find("span",{"class": "infoValueFullBath"}).find("b").text
        except:
            d["FullBaths"]=None
        
        try:
            d["HalfBaths"]=item.find("span",{"class": "infoValueHalfBath"}).find("b").text
        except:
            d["HalfBaths"]=None

        for column_group in item.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if 'Lot Size' in feature_group.text:
                    d["LotSize"]=feature_name.text

        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("result.csv")