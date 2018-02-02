
# Packages you will need are,
# * pandas
# * matplotlib

import matplotlib.pyplot as plt
import pandas as pd

import datetime


# We will start off by creating  a dataframe from Weather Underground Data retreived from the url below.

#df = pd.read_csv('http://cs1656.org/data/KPIT_Aug17.csv', sep=',', engine='python', parse_dates=['EST'])


# To display the top 'n' rows of the dataframe, use the head() command below. The default is 5 rows.
#df.head()


# Now to find all the column names of the dataframe and their data types, type the following command.
#df.dtypes

# There are two ways to access a dataframe column. 
# The first way is accessing it like a dictionary as shown below. We will be using head function to show the first few rows only.
#df['EST'].head()


# The second way is to access using dot. But this only works if the column name is a valid variable name without any spacing.
#df.EST.head()


# You can also access multiple columns by passing list of column names.
#df[['EST','Mean TemperatureF']].head()


# Now lets start with basic plotting in Python first. We will use the plot function. Note that plot returns a tuple of handle and labels. If you need the plot handle in the future you will assign a variable to the plot function's return value.
#p1 = plt.plot(df['EST'],df['MeanDew PointF'])
#p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
#plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

#plt.show()


# Initializing a larger figure
#fig = plt.figure(figsize=(10, 6))

# Plotting
#p1 = plt.plot(df['EST'],df['MeanDew PointF'])
#p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
#plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

# Formatting graph
#plt.xticks(rotation = 90, fontsize = 8)
#plt.xlabel('Date')
#plt.ylabel('Mean Temperature')
#plt.title('Mean Tempertaures for August 2017')

# Saves figure 
#plt.savefig("basic_plot.png")

#plt.show()


# Bar Plot
#fig = plt.figure(figsize=(10, 6))
#plt.bar(range(len(df['EST'])),df['Mean Humidity'], align = 'center')

# Formatting graph
#plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'), rotation = 90, fontsize = 8)
#plt.xlabel('Date')
#plt.ylabel('Mean Humidity')
#plt.title('Mean Humidity for August 2017')

# Saves figure
#plt.savefig("bar_plot.png")

#plt.show()


# Now, lets try to plot the two graphs above on the same figure using subplots. The code for plotting is the same as that shown above. 
#fig = plt.figure(figsize=(10, 16))

# Subplot of basic graph
#plt.subplot(211) # first 2 = 2 plots, one top, one bottom, third 1 refers to first(top plot)
#p1 = plt.plot(df['EST'],df['MeanDew PointF'])
#p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
#plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

#plt.xticks(rotation = 90, fontsize = 8)
#plt.xlabel('Date')
#plt.ylabel('Mean Temperature')
#plt.title('Mean Tempertaures for August 2017')

# Subplot of bar graph graph
#plt.subplot(212) # first 2 = 2 plots, one top, one bottom, third 2 refers to second(bottom plot)
#plt.bar(range(len(df['EST'])),df['Mean Humidity'], align = 'center')

#plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'), rotation = 90, fontsize = 8)
#plt.xlabel('Date')
#plt.ylabel('Mean Humidity')
#plt.title('Mean Humidity for August 2017')

# Saves figure
#plt.savefig("subplot_basic_bar.png")

#plt.show()


# Subplots allows us to establish relationships between different variables and different statistics. 
# 
# Scatter Plot
#fig = plt.figure(figsize=(10, 6))

#plt.scatter(df['Max TemperatureF'],df['Min TemperatureF'])

# Formatting graph
#plt.xlabel('Max Temperture')
#plt.ylabel('Min Temperature')
#plt.title('Min and Max Temperature for August 2017')

#Saves figure
#plt.savefig("scatter_plot.png")

#plt.show()


# The graph above shows us that min and max temperature have a strong positive correlation.

# ## Tasks
# For your tasks, the input file is available at http://cs1656.org/data/top12cities.csv. The file consists of population density estimates and land area of several cities in USA. 
# 
# You need to read the file into a dataframe and perform the following three tasks during the recitation. 
#
print("\nRead CSV from web address.")
dataframe = pd.read_csv('http://cs1656.org/data/top12cities.csv', sep=',', engine='python')

print("\nPrint dataframe column name and data types:")
print(dataframe.dtypes)

# **Task 1** 
# Plot a scatter plot of with 'land area' on the x-axis and '2014 estimate' on the y-axis. After observing the plot, do you think the two variables are strongly or weakly correlated? Is the correlation positive or negative?
print("\nInitialize fig size.")
plt.figure(figsize=(10, 6))

print("Grab axis data.")
#                        X AXIS                    Y AXIS
plt.scatter(dataframe['2014 land area'], dataframe['2014 estimate'])

# Formatting graph
print("Format graph.")
plt.xlabel('2014 Land Area')
plt.ylabel('2014 Population Desnity Estimate')
plt.title('Land Area and Estimate Population Desnity for 2014')

#Saves figure
#plt.savefig("scatter_plot.png")

print("Display plot.")
#plt.show()


# **Task 2** 
# Plot a bar plot showing each city's 2014 population estimate given by '2014 estimate' column. 

# Bar Plot
print("\nSet figure size.")
fig = plt.figure(figsize=(9, 6))

print("Grab axis data.")
#                X Axis                   Y Axis
plt.bar(dataframe['City'], dataframe['2014 estimate'], align = 'center')

# Formatting graph
print("Formatting plot.")
plt.xticks(dataframe['City'], rotation = 90, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population Estimate')
plt.title('2014 City Populations')


# Saves figure
#plt.savefig("bar_plot.png")

print("Display plot.")
plt.show()

# **Task 3** 
# 
# Now that you plotted a simple bar plot, try plotting a grouped bar plot that shows both 2010 and 2014 estimate for each city on the same plot. This means that there will be two grouped bars per city on your graph. 



fig = plt.figure(figsize=(5, 5))

# Subplot of basic graph
plt.subplot() 
p1 = plt.bar(dataframe['City'], dataframe['2014 estimate'], align = 'center')
p2 = plt.bar(dataframe['City'], dataframe['2010 Census'], align = 'center')
plt.legend([p1[0],p2[0]], ['2014 estimate', '2010 census'])

plt.xticks(dataframe['City'], rotation = 90, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population Estimate')
plt.title('2014 City Populations')

print("Display plot.")
plt.show()