import os
from datetime import date

today = date.today()

date = today.strftime("%B %d, %Y")
print("Date: ", date, "\n\n")

import pandas as pd

dfs = pd.read_html('https://www.mohfw.gov.in/')
for df in dfs:
    pass

df = df.drop([29])

print('Data Table Read Completed')

import json

a_file = open("C:\\Users\\Chaitanya\\Desktop\\CoronaVisualization\\india.json", "r")
json_object = json.load(a_file)
a_file.close()

print("JSON File Opened")

for i in range(0, 29):
    for j in range(0, 29):
        if df['Name of State / UT'][i] == json_object['data'][j]['name'] :
            json_object['data'][j]['dead'] = str(df.at[i,'Death'])
            json_object['data'][j]['infected'] = str(df.at[i,'Total Confirmed cases (Including 51 foreign Nationals)'])
            json_object['data'][j]['recovered'] = str(df.at[i,'Cured/Discharged/Migrated'])
            json_object['data'][j]['sick'] = str(int(df.at[i,'Total Confirmed cases (Including 51 foreign Nationals)']) - (int(df.at[i,'Death']) + int(df.at[i,'Cured/Discharged/Migrated'])))
            json_object['data'][j]['lastUpdated'] = date
            break


a_file = open("C:\\Users\\Chaitanya\\Desktop\\CoronaVisualization\\india.json", "w")
json.dump(json_object, a_file)
a_file.close()


df2 = pd.DataFrame(df)
df2 = df2.rename(columns={"Name of State / UT": "name", "Total Confirmed cases (Including 51 foreign Nationals)": "infected"})
df2.to_json(r'piechart.json',orient='records')

print("JSON Updated")