import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_file(filename):
    '''This function takes file name as argument and returns DataFrame one with years 
    as columns and one with countries as columns and prints the data'''
    
    read_data = pd.read_csv(filename) # reads csv data 
        
    names = read_data['Country Name'] # printing the country name
    
    numeric_columns = read_data._get_numeric_data().columns.values.tolist() # taking Years columns
    
    years_df = pd.DataFrame({"Years" : numeric_columns})
    
    countrynamedf = pd.DataFrame({'Countries':names.unique()}) # unique values from column : country
         
    t_countrydf = countrynamedf.set_index('Countries').transpose() 
    
    t_columndf = years_df.set_index('Years').transpose()
        
    return t_countrydf, t_columndf, read_data

t_countrydf,t_columndf,read_data = load_file(r"C:\Users\koush\Downloads\API_19_DS2_en_csv_v2_4700503.csv") 

read_data

def values_axis(indicator):
    forest_area = read_data[read_data['Indicator Code'] == indicator]
    country_codes = forest_area.set_index('Country Code')
    data_selected = country_codes.loc[["SAS", "IND", "CHN", "ZAF", "PAK", "USA"], ['Country Name', '2000', '2001', '2002', '2003', '2004', '2005', '2006']]  
    return data_selected

''' total population of bar plot '''

all_values_totalpol = values_axis("SP.POP.TOTL")


bargraph_forest = all_values_totalpol.plot.bar(x = 'Country Name', y = None,fontsize='12', title = "Total Population",width = 0.6, edgecolor='blue')

plt.legend(loc = 0)

plt.show()


''' GreenHousegas emission Bar plot'''

greenhouse_df = values_axis("EN.ATM.GHGT.ZG")

bargraph_greenhouse = greenhouse_df.plot.bar(x = 'Country Name', y = None,fontsize='12', title = "GreenHouse Gas Emission",width = 0.8, edgecolor='blue')

plt.legend(loc = 0)

plt.show()

''' Correlation'''

''' Mean and Median of the data for the total population the world'''

dataframe_mean = all_values_totalpol.mean() # Gives
print(dataframe_mean)
dataframe_median = all_values_totalpol.median()
print(dataframe_median)

xdata=['2000','2001', '2002', '2003', '2004', '2005', '2006']  
y_mean = ['6.966067e+08', '7.066986e+08', '7.166145e+08', '7.263613e+08', '7.360363e+08', '7.456488e+08', '7.551682e+08']
y_median = ['669368979.5', '679984524.5', '690471190.0', '700815539.5', '711214382.0', '721563261.5', '731933101.5']

plt.barh(xdata, y_mean, color = 'green')
plt.title('Mean of the total population accordingly to years', fontsize = 15, color = 'Blue')
plt.xticks(rotation=45)
plt.show()

plt.bar(xdata,y_median, color = 'orange')
plt.title('Median of the total population accordingly to years', fontsize = 15, color = 'Blue')
plt.xticks(rotation=45)
plt.show()

