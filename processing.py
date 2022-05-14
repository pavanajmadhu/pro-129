from numpy.typing import _256Bit
import pandas as pd
import csv




#Mass=rows[2]
df=pd.read_csv("dataset_2_sorted.csv")
df=df[df["Distance"].notna()]
df=df[df["Mass"].notna()]
df=df[df["Radius"].notna()]

Mass=df["Mass"]
Radius=df["Radius"]

planet_radius=[]
planet_mass=[]

for i in Mass:
    solar=Mass*0.000954588
    planet_mass.append(solar)

for i in Radius:
    solar1=Radius*0.102763
    planet_radius.append(solar1)


with open("want_to_merge.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(planet_mass) 
    csvwriter.writerows(planet_radius)