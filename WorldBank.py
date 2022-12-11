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
