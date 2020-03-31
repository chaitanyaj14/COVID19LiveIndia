from datetime import date

today = date.today()

date = today.strftime("%B %d, %Y")
print("Date: ", date, "\n\n")

import pandas as pd

dfs = pd.read_html('https://www.mohfw.gov.in/')
for df in dfs:
    pass

df = df.drop([27])
df = df.drop([28])

import json

a_file = open("india.json", "r")
json_object = json.load(a_file)
a_file.close()

for i in range(0, 27):
    for j in range(0, 27):
        if df['Name of State / UT'][i] == json_object['data'][j]['name'] :
            json_object['data'][j]['dead'] = df.at[i,'Death']
            json_object['data'][j]['infected'] = df.at[i,'Total Confirmed cases *']
            json_object['data'][j]['recovered'] = df.at[i,'Cured/Discharged/Migrated']
            json_object['data'][j]['sick'] = str(int(df.at[i,'Total Confirmed cases *']) - (int(df.at[i,'Death']) + int(df.at[i,'Cured/Discharged/Migrated'])))
            json_object['data'][j]['lastUpdated'] = date

a_file = open("india.json", "w")
json.dump(json_object, a_file)
a_file.close()

df2 = pd.DataFrame(df)
df2 = df2.rename(columns={"Name of State / UT": "name", "Total Confirmed cases *": "infected"})
df2.to_json(r'piechart.json',orient='records')