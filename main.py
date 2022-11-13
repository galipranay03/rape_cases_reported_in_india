# import the libraries

# import inline as inline
import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import plotly.express as px
import seaborn as sns
# %matplotlib inline

# victims of rape Dataframe

mydata = pd.read_csv("C:\\Users\\galip\\Downloads\\20_Victims_of_rape.csv")
df = pd.DataFrame(mydata)
print(df.to_string()) #let's see how the data is structured

print('-> HEAD()===============================================================================================================')

# let's print the first five rows in csv file
# for that we use the head() method
# default it shows first 5 rows, but when we add a value init it's show the particular values,
# from first to that particular value.
# suppose we add a value 20, It shows the first 20 Rows data:

print(df.head())

print('-> TAIL()===============================================================================================================')

# let's print the last five rows in csv file
# for that we use the tail() method
# default it shows last 5 rows, but when we add a value init it's show the particular values,
# suppose we add a value 15, It shows last 15 Rows Data:

print(df.tail())

print('-> INFO()===============================================================================================================')

# now check the general information of the DATASET
# the info() method is used to give general information
# of dataset by columns like observation number and data types in coloums.
# The information contains the number of columns, column labels, column data types,
# memory usage, range index, and the number of cells in each column (non-null values).

print(df.info())

print('-> D-TYPES===============================================================================================================')
# check the data types
# int
# objects
# for that we use dtypes method

print(df.dtypes)

print('-> TAKE SOME COLUMNS ===============================================================================================================')

# let's separate the data into some columns like
# Area_name, year, victims of rape total
# take a variable called specific_column,
# and put three columns in it

specific_columns = df[['Area_Name','Year','Victims_of_Rape_Total']]
print(specific_columns)

print('-> FIND SLICING ===============================================================================================================')

# find the particular dataset by using slicing
# if we want the data from 1 to 100 rows, we use slice
# slice starts from 0.
# let's print the first 100 rows

using_slicing =specific_columns[:100] # using slicing
print(using_slicing)

print('-> VALUE_COUNT()===============================================================================================================')

# find the value of each column by using value_count
# it will show the value of each column
# let's find out how it will work

data_count = mydata[['Area_Name','Year']].value_counts()
print(data_count.head())

print('-> DATATYPES===============================================================================================================')

# find the types of the data by using dtypes

print(mydata.dtypes)

print('-> GROUP_BY===============================================================================================================')

total_victims = mydata.groupby(['Area_Name','Year'])['Victims_of_Rape_Total'].sum().reset_index()
print(total_victims)

print('-> NEW_COLUMN===============================================================================================================')

# let's plot the unreported rape cases sorted by states throughout 2001 to 2010
# let's store the number of unreported rape cases in another column

mydata['Unreported_Cases'] = mydata['Victims_of_Rape_Total']-mydata['Rape_Cases_Reported']

# let's see how the dataframe came
print(mydata[mydata['Unreported_Cases']>0].head())

print('-> BAR_GRAPH===============================================================================================================')

# let's plot the unreported rape cases sorted by states throughout 2001 to 2010

unreported_victims_by_state = mydata.groupby('Area_Name').sum()
unreported_victims_by_state.drop('Year', axis = 1, inplace = True)

# let's finally plot it
plt.subplots(figsize = (16, 5))
ct = unreported_victims_by_state[unreported_victims_by_state['Unreported_Cases']
                                 > 0]['Unreported_Cases'].sort_values(ascending = False)
# print(ct)
# bg means BARGRAPH
bg = ct.plot.bar() #select the graph model, for me i am using bar
bg.set_xlabel('Area Name')
bg.set_ylabel('Total Number of Unreported Rape Victims from 2001 to 2010')
bg.set_title('Statewise total Unreported Rape Victims throughout 2001 to 2010')
plt.show()

print('-> GENERAL_DATA==============================================================================================================')

# let's take some general data and plot some simple charts

rape_victims_by_state = mydata.groupby('Area_Name').sum()
rape_victims_by_state.drop('Year', axis = 1, inplace = True)
print('Total Rape Victims = ' ,rape_victims_by_state['Rape_Cases_Reported'].sum())
print(rape_victims_by_state.sort_values(by = 'Rape_Cases_Reported', ascending = False).head())

print('-> HEATMAP===============================================================================================================')

# let's make a heatmap variable
rape_victims_heatmap = rape_victims_by_state.drop(['Rape_Cases_Reported',
                                                   'Victims_of_Rape_Total',
                                                   'Unreported_Cases'], axis = 1)
plt.subplots(figsize = (10, 10))
ax = sns.heatmap(rape_victims_heatmap, cmap="Greens")
ax.set_xlabel('Age Group')
ax.set_ylabel('State Name')
ax.set_title('Statewise Victims of Rape Cases based on Age Group')
plt.show()

print('->SUB_PLOTS ===============================================================================================================')

# let's first plot only the total number of rape cases reported in each state
plt.subplots(figsize = (15, 6))
ct = rape_victims_by_state['Rape_Cases_Reported'].sort_values(ascending = False)

#print(ct)
ax = ct.plot.bar()

#ax = sns.barplot(x = rape_victims_by_state.index, y = rape_victims_by_state['Rape_Cases_Reported'])
ax.set_xlabel('Area Name')
ax.set_ylabel('Total Number of Reported Rape Victims from 2001 to 2010')
ax.set_title('Statewise total Reported Rape Victims throught the Years 2001 to 2010')
plt.show()
print(ct)

print('-> MP===============================================================================================================')

# let's look at the Madhya Pradesh data
mp_rape_victims = mydata[mydata['Area_Name'] == 'Madhya Pradesh']

# let's have a look in the data
print(mp_rape_victims.head())

print('-> TOTAL CASES REPORTED IN MP===============================================================================================================')

# Let's have a look at yearly distribution of number of rape victims in Madhya Pradesh
mp_rape_victims_by_year = mp_rape_victims.groupby('Year').sum()

# plotting the data

plt.subplots(figsize = (15, 6))
ax = mp_rape_victims_by_year['Rape_Cases_Reported'].plot()
ax.xaxis.set_ticks(np.arange(2001, 2011, 1)) #numpy
ax.set(xlabel = 'Year', ylabel = 'Total Number of Reported Rape Victims',
       title = 'Number of Rape Victims throught the years 2001 to 2010 of Madhya Pradesh')
plt.show()

print('===============================================================================================================')

# let's first see the mp_rape_victims dataframe
# mp_rape_victims.head()

# plot the dataframe
mp_incest_rape_cases = mp_rape_victims[mp_rape_victims['Subgroup'] == 'Victims of Incest Rape']
plt.subplots(figsize = (15,6))
ct = mp_incest_rape_cases.groupby('Year').sum()
ax = ct['Rape_Cases_Reported'].plot.bar()
for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x()+0.1, p.get_height()+2),fontsize=12)
ax.set_xlabel('Year')
ax.set_ylabel('Total Number of Incest Rape Victims from 2001 to 2010')
ax.set_title('Total Reported Incest Rape Victims of Madhya Pradesh throught the Years 2001 to 2010')
plt.show()

print('===============================================================================================================')

wb_rape_victims = mydata[mydata['Area_Name'] == 'West Bengal']

# Let's have a look at yearly distribution of number of rape victims in Madhya Pradesh
wb_rape_victims_by_year = wb_rape_victims.groupby('Year').sum()

# plotting the data
plt.subplots(figsize = (15, 6))
ax = wb_rape_victims_by_year['Rape_Cases_Reported'].plot()
ax.xaxis.set_ticks(np.arange(2001, 2011, 1))
ax.set(xlabel = 'Year', ylabel = 'Total Number of Reported Rape Victims',
       title = 'Number of Rape Victims throught the years 2001 to 2010 of West Bengal')
plt.show()

print('===============================================================================================================')

# let's calculate the percentage increase of number of rapes in West Bengal and compare
# it with Madhya Pradesh

plt.subplots(figsize = (15, 6))
ax = (wb_rape_victims_by_year['Rape_Cases_Reported'].pct_change() * 100).plot(legend = True,
                                                                              label = 'West Bengal')
(mp_rape_victims_by_year['Rape_Cases_Reported'].pct_change() * 100).plot(ax = ax, legend = True,
                                                                         label = 'Madhya Pradesh')
ax.set(xlabel = 'Year', ylabel = 'Percent',
       title = 'Yearly increase and decrease in number of rapes in West Bengal and Madhya Pradesh')
ax.axhline(0, color = 'black')
ax.axvline(2002, color = 'black')
plt.show()
print('Overall Increase in number of rapes in West Bengal =',
      '{0:.2f}'.format(((wb_rape_victims_by_year.iloc[9]['Rape_Cases_Reported']
                         - wb_rape_victims_by_year.iloc[0]['Rape_Cases_Reported'])
                        /wb_rape_victims_by_year.iloc[9]['Rape_Cases_Reported']) * 100), 'Percent')
print('Overall Increase in number of rapes in Madhya Pradesh =',
      '{0:.2f}'.format(((mp_rape_victims_by_year.iloc[9]['Rape_Cases_Reported']
                         - mp_rape_victims_by_year.iloc[0]['Rape_Cases_Reported'])
                        /wb_rape_victims_by_year.iloc[9]['Rape_Cases_Reported']) * 100), 'Percent')

print('===============================================================================================================')

# incest rape cases in Bengal

wb_incest_rape_cases = wb_rape_victims[wb_rape_victims['Subgroup'] == 'Victims of Incest Rape']
plt.subplots(figsize = (15,6))
ct = wb_incest_rape_cases.groupby('Year').sum()
ax = ct[ct['Rape_Cases_Reported'] > 0]['Rape_Cases_Reported'].plot.bar()
for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x() + .15, p.get_height()+1),fontsize=13)
ax.set_xlabel('Year')
ax.set_ylabel('Total Number of Incest Rape Victims from 2001 to 2010')
ax.set_title('Total Reported Incest Rape Victims of West Bengal throught the Years 2001 to 2010')
plt.show()
