
# coding: utf-8

# # CS 1656 – Introduction to Data Science (Spring 2018) 
# 
# ## Instructor: Alexandros Labrinidis / Teaching Assistant: Evangelos Karageorgos
# 
# ### Additional Credits: Zuha Agha, Anatoli Shein, Phuong Pham
# ---
# In this recitation you will be learning pandas dataframe basics and plotting in Python. Packages you will need are,
# * pandas
# * matplotlib
# 
# First step is to import the packages above. If import fails, it means that the package is not installed. 

# In[ ]:

import matplotlib.pyplot as plt
import pandas as pd
import datetime


# For the sake of interactive display in Jupyter, we will enable matplotlib inline.

# In[ ]:

get_ipython().magic('matplotlib inline')


# ## Dataframe Basics
# 
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table. DataFrame accepts many different kinds of input:
# *Dict of 1D ndarrays, lists, dicts, or Series
# *2-D numpy.ndarray
# *Structured or record ndarray
# *A Series
# *Another DataFrame
# 
# Along with the data, you can optionally pass index (row labels) and columns (column labels) arguments.
# 
# Now what is a Series?
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). You can think of it as a 1-dimensional dataframe. Series objects can also have index. 
# ### Creating a Dataframe
# We will start off by creating  a dataframe from Weather Undergraound Data retreived from the url below.

# In[ ]:

df = pd.read_csv('http://cs1656.org/data/KPIT_Aug17.csv',                       sep=',', engine='python', parse_dates=['EST'])


# To display the top 'n' rows of the dataframe, use the head() command below. The default is 5 rows.

# In[ ]:

df.head()


# Now to find all the column names of the dataframe and their data types, type the following command.

# In[ ]:

df.dtypes


# Notice the type of 'EST' column. We will find out why that's relevant a few steps later.
# ### Accessing Dataframe Columns
# There are two ways to access a dataframe column. 
# The first way is accessing it like a dictionary as shown below. We will be using head function to show the first few rows only.

# In[ ]:

df['EST'].head()


# The second way is to access using dot. But this only works if the column name is a valid variable name without any spacing.

# In[ ]:

df.EST.head()


# You can also access multiple columns by passing list of column names.

# In[ ]:

df[['EST','Mean TemperatureF']].head()


# ---
# ## Plotting
# ### Basic Plot

# Now lets start with basic plotting in Python first. We will use the plot function. Note that plot returns a tuple of handle and labels. If you need the plot handle in the future you will assign a variable to the plot function's return value.

# In[ ]:

p1 = plt.plot(df['EST'],df['MeanDew PointF'])
p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

plt.show()


# That does not look too pretty. Let's format the graph and plot again. 

# In[ ]:

# Initializing a larger figure
fig = plt.figure(figsize=(10, 6))

# PLotting
p1 = plt.plot(df['EST'],df['MeanDew PointF'])
p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

# Formatting graph
plt.xticks(rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Temperature')
plt.title('Mean Tempertaures for August 2017')

# Are we ready to show the formatted graph now? Not yet. Because we want
# to save our graph figure this time.In order to use the save command, it
# is important to save before the show command because the show command
# clears the axis of the figure after displaying.

plt.savefig("basic_plot.png")
plt.show()


# ### Bar Plot

# In[ ]:

fig = plt.figure(figsize=(10, 6))
plt.bar(range(len(df['EST'])),df['Mean Humidity'], align = 'center')

# Formatting graph
plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'),               rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Humidity')
plt.title('Mean Humidity for August 2017')

plt.savefig("bar_plot.png")
plt.show()


# Now, lets try to plot the two graphs above on the same figure using subplots. The code for plotting is the same as that shown above. 

# In[ ]:

fig = plt.figure(figsize=(10, 16))

# Subplot of basic graph
plt.subplot(211)
p1 = plt.plot(df['EST'],df['MeanDew PointF'])
p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])

plt.xticks(rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Temperature')
plt.title('Mean Tempertaures for August 2017')

# Subplot of bar graph graph
plt.subplot(212)
plt.bar(range(len(df['EST'])),df['Mean Humidity'], align = 'center')

plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'),               rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Humidity')
plt.title('Mean Humidity for August 2017')

plt.savefig("subplot_basic_bar.png")
plt.show()


# What is teh advantage of subplots? It allows us to establish relationships between different variables and different statistics. Looking at the two subplots above, do you notice any relationship?
# 
# ### Scatter Plot
# Scatter plots are commonly used to show correlation between variables. If the data points make a straight line going from the origin out to high x and high y values, then the variables are said to have a positive correlation. If the line goes from a high value on the y-axis down to a high value on the x-axis, the variables have a negative correlation. The closer the data points in the scatter plot, the higher the correlation between the two variables, or the stronger the relationship.

# In[ ]:

fig = plt.figure(figsize=(10, 6))

plt.scatter(df['Max TemperatureF'],df['Min TemperatureF'])

# Formatting graph
plt.xlabel('Max Temperture')
plt.ylabel('Min Temperature')
plt.title('Min and Max Temperature for August 2017')

plt.savefig("scatter_plot.png")
plt.show()


# The graph above shows us that min and max temperature have a strong positive correlation.

# ## Tasks
# For your tasks, the input file is available at http://cs1656.org/data/top12cities.csv. The file consists of population density estimates and land area of several cities in USA. 
# 
# You need to read the file into a dataframe and perform the following three tasks during the recitation. 
# 
# **Task 1** 
# 
# Plot a scatter plot of with 'land area' on the x-axis and '2014 estimate' on the y-axis. After observing the plot, do you think the two variables are strongly or weakly correlated? Is the correlation positive or negative?
# 
# **Task 2** 
# 
# Plot a bar plot showing each city's 2014 population estimate given by '2014 estimate' column. 
# 
# **Task 3** 
# 
# Now that you plotted a simple bar plot, try plotting a grouped bar plot that shows both 2010 and 2014 estimate for each city on the same plot. This means that there will be two grouped bars per city on your graph. 
