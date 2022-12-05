import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas_datareader as pdr #pdr.get_data_fred('GS10')
# from pandas_datareader import pdr
import wbgapi as wb




wb.series.metadata.get('AG.LND.FRST.ZS')

Data = wb.data.DataFrame('AG.LND.FRST.ZS', ["USA", "DEU", "CHN", "CAN", "BRA", "JPN", "NPL", "IND", "IDN", "WLD"],range(1990, 2020))

df = pd.melt(id_vars= 'Country', var_name='years',value_name='economy')

print(df)




wb.data.DataFrame('EN.ATM.GHGT.ZG', 
                  economy=wb.region.members('SAS'),
                  time=range(1990, 2020), numericTimeKeys=True,
                  labels=True).set_index('Country').transpose().plot(title='Forest Area')


# https://data.worldbank.org/indicator/AG.LND.AGRI.ZS  - Agricultural land (% of land area)

# https://data.worldbank.org/indicator/AG.LND.FRST.ZS  -  Forest area (% of land area)
# https://data.worldbank.org/indicator/EN.ATM.GHGT.ZG  -  Total greenhouse gas emissions (% change from 1990)

# List of indicators according to the features defined above
# INDICATOR_CODES=['AG.LND.FRST.ZS', 'EN.ATM.GHGT.ZG']


# CountryNames = ["USA", "DEU", "CHN", "CAN", "BRA", "JPN", "NPL", "IND", "IDN", "WLD"]

# Forest_area = pdr.     

# (name = 'AG.LND.FRST.ZS', country = CountryNames, start = 1990, end = 2019)

# # download(indicator = 'AG.LND.FRST.ZS', country = CountryNames, start = 1990, end = 2019)
# # GreenHouse_emission = pdr.download(indicator = 'EN.ATM.GHGT.ZG', country = CountryNames, start = 1990, end = 2019)


# print(Forest_area)
# # print(GreenHouse_emission)









# WorldBank = pd.read_excel(r"D:\Ramya\2ndAssign\P_Data_Extract_From_World_Development_Indicators.xlsx")
# print(WorldBank.describe())    #iloc[:,1:3].mean)

# import requests



# url = 'http://api.worldbank.org/v2/country/%s/indicator/NY.GDP.PCAP.CD?format=json'
# countries = ["DZA","AGO","ARG","AUS","AUT","BEL","BRA","CAN","CHL","CHN","COL","CYP", "CZE","DNK","FIN","FRA","GEO","DEU",
#           "GRC","HUN","ISL","IND","IDN","IRL","ISR","ITA","JPN","KAZ","KWT","LBN","LIE","MYS","MEX","MCO","MAR","NPL","NLD",
#           "NZL","NGA","NOR","OMN","PER","PHL","POL","PRT","QAT","ROU","SGP","ZAF","ESP","SWE","CHE","TZA","THA","TUR","UKR",
#           "GBR","USA","VNM","ZWE"]
    
# my_values = []
# for country in countries:
#     data = requests.get(url %country).json()

#     try:
#         for d in data[1]:
#             my_values.append({
#                 'country':d['country']['value'],
#                 'date':d['date'],
#                 'value':d['value']
#             })
#     except Exception as err:
#         print(f'[ERROR] country ==> {country} error ==> {err}')

# pd.DataFrame(my_values).sort_values(['country', 'date'], ascending=True)