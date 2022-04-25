import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"
r = requests.get(URL)

html_text = r.text

# Parsing HTML into text format:
soup = BeautifulSoup(html_text, 'html.parser')

# Finding the first table which has the actual data:
table = soup.find_all('table')[0]

# Finding rows of the table:
table_rows = table.find_all('tr')

# Finding the actual row value from where the countries are listed:
for i in range(len(table_rows)):
    if "USA" in table_rows[i].text:
        row_start_val = i

# dict_val will store all the data set.
dict_val = {}

for i in range(row_start_val, len(table_rows)):
    # Inner dictionary will store data of each country.
    inner_dict = {}
    inner_arr = []

    # row_val is storing the data of each country.
    row_val = table_rows[i].text

    # Total resembles the end of the table.
    if "Total:" in table_rows[i].text:
        break

    row_val_list = row_val.strip().split('\n')

    for k in range(2, len(row_val_list)):
        inner_arr.append(row_val_list[k])

    inner_dict["Total Cases"] = inner_arr[0]
    inner_dict["Total Deaths"] = inner_arr[2]
    inner_dict["Total Recovered"] = inner_arr[4]
    inner_dict["Active Cases"] = inner_arr[6]

    dict_val[row_val_list[1]] = inner_dict

with open("covid_data.json", "w") as outfile:
    json.dump(dict_val, outfile)
