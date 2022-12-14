# importing the libraries to the current environment
import pandas as pd # Python to bring the pandas data analysis
import matplotlib.pyplot as plt # collection of functions and visualization package Matplotlib
# some additional plot types and provides some visual improvements to some plots and graphs
import seaborn as sns

# Intializing the indicators to the list    
indicator = ['Forest area (sq. km)',
             'Urban population', 
             'Agricultural land (% of land area)', 
             'Cereal yield (kg per hectare)', 
             'CO2 emissions (kt)', 
             'Population growth (annual %)', 
             'Agricultural land (sq. km)']

# Taking the specific years into the year variable
year = ['2000', '2001', '2002', '2003', '2004', '2005', '2006']

   
def load_file(filename):
    '''This function takes file name as argument and returns DataFrame one with years 
        as columns and one with countries as columns and prints the data
        filename : local path of the filename
    '''
    read_data = pd.read_csv(filename) # reads csv data  
    countries = read_data # copying the file into a variable countries
    # dropping the columns to print the data to set the countries as index
    country_new = countries.drop(['Sl No', 'Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    countries_ind = country_new.set_index('Country Name') #setting the index as countries
    year_ind = countries_ind.transpose().reset_index() # transposing and resetting the index
    # setting the index as years as columns
    year_ind = year_ind.rename(columns={"index":"Year"}).set_index('Year')   
    return year_ind, countries_ind, read_data # returning the data


# loading the values to dataframe
year_ind, countries_ind, read_data = load_file(r"C:\Users\koush\Downloads\API_19_DS2_en_csv_v2_4700503.csv")
print(read_data) # printing the dataframe


def values_axis(indicator):
    '''Getting the list of indicator codes for the countries and years  
        indicator : Code of the indicators in world bank
    '''
    indi = read_data[read_data['Indicator Code'] == indicator] # intializing the indicator
    country_codes = indi.set_index('Country Code') # setting the index for country code
    # setting the values for the specific data of years and country codes
    data_selected = country_codes.loc[["SAS", "IND", "CHN", "ZAF", "PAK", "USA"], 
                                      ['Country Name', '2000', '2001', '2002',
                                       '2003', '2004', '2005', '2006']]           
    return data_selected


def heatmap(countryname): 
    ''' Defining the function for the heatmap based on country with a corelation of indicator names
        countryname : providing the country name from dataframe
    '''
    # setting the countryname from dataframe
    Countryname = read_data[read_data['Country Name'] == countryname]  
    heatmap_data = Countryname.set_index('Indicator Name') # setting the index for country code
    heatmap_data = heatmap_data.loc[indicator,year].transpose() # Transpose the data
    #plotting the heatmap
    sns.heatmap(heatmap_data.corr(), cmap = 'Accent', linewidths = 0.1, annot = True) 
    plt.show() # showing the plot
    

    
#-------------------------------------------------------------------------

# Bar plot 1

# total population of bar plot by the years
all_values_totalpol = values_axis("SP.POP.TOTL") # getting the data from the indicator codes
# bar graph plotting using dataframe for the country
bargraph_forest = all_values_totalpol.plot.bar(x = 'Country Name', 
                                               y = None, fontsize = '12', 
                                               title = "Total Population", 
                                               width = 0.6, edgecolor = 'blue')
plt.legend(loc = 0) # legend values and spacing
plt.show() # plots the bar graph


#-------------------------------------------------------------------------

# Bar plot 2

# GreenHousegas emission Bar plot
greenhouse_df = values_axis("EN.ATM.GHGT.ZG") # getting the data from the indicator codes
# bar graph plotting
bargraph_greenhouse = greenhouse_df.plot.bar(x = 'Country Name',
                                             y = None, fontsize = '12', 
                                             title = "GreenHouse Gas Emission", 
                                             width = 0.8, edgecolor = 'blue')

plt.legend(loc = 0) # labelling legend values 
plt.show() # plots the bar graph


#-------------------------------------------------------------------------

''' 
    Correlation : Mean and Median of the data for the indicator name : total population the world 
'''

dataframe_mean = all_values_totalpol.mean() # Gives the mean value of total population
print(dataframe_mean)
dataframe_median = all_values_totalpol.median() # Gives the median value of total population
print(dataframe_median)

''' 
    Took the data from the Mean and Median of the data for the 
    indicator name : total population the world as xdata as years
    y_mean as the mean of total population and 
    y_median as the median of total population
    
'''
xdata = ['2000', '2001', '2002', '2003', '2004', '2005', '2006']
# mean of total population
y_mean = ['6.966067e+08', '7.066986e+08', '7.166145e+08', '7.263613e+08', 
          '7.360363e+08', '7.456488e+08', '7.551682e+08']
# median of total population
y_median = ['669368979.5', '679984524.5', '690471190.0', '700815539.5',
            '711214382.0', '721563261.5', '731933101.5']
#-------------------------------------------------------------------------

# Bar plot 3

# plotted the horizantal bar graph for the mean data
plt.barh(xdata, y_mean, color = 'green') # plotting of bar chart
# title of the bar graph
plt.title('Mean of the total population accordingly to years', fontsize = 15, color = 'Blue')
plt.xticks(rotation=45)
plt.show() # plots the bar graph

#-------------------------------------------------------------------------

# Bar plot 4

# plotted the horizantal bar graph for the median data
plt.bar(xdata,y_median, color = 'orange') # plotting of bar chart
# title of the bar graph
plt.title('Median of the total population accordingly to years', fontsize = 15, color = 'Blue')
plt.xticks(rotation=45)
plt.show() # plots the bar graph


#-------------------------------------------------------------------------


'''
     Heatmap : correlations of between two countries for some specfic indicators
     from the definition of heatmap, provided the country and plotted the heatmap    

'''
# heat map 1

# heatmap of country India    
heatmap('India')


# heat map 2

# heatmap of country China
heatmap('China')
