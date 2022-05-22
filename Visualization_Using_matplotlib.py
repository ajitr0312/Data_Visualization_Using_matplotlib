#!/usr/bin/env python
# coding: utf-8

# ## <center> Visualization Using Matplotlib</center>
# 
# ### <center> Practice Questions with Solutions</center>

# <b>Q. No. 1</b> Load the necessary package for plotting using pyplot from matplotlib. 
# - Example - Days(x-axis) represents 8 days and Speed represents a car’s speed. Plot a Basic line plot between days and car speed, put x axis label as days and y axis label as car speed and put title Car Speed Measurement.
#           -- Days=[1,2,3,4,5,6,7,8]
#          -- Speed=[60,62,61,58,56,57,46,63]

# In[1]:


import matplotlib.pyplot as plt #Importing the required library

Days = [1,2,3,4,5,6,7,8]
Speed = [60,62,61,58,56,57,46,63]

plt.figure(figsize=[8,6])
plt.plot(Days, Speed, color = 'Red')
plt.xlabel("Days")
plt.ylabel("Speed")
plt.title("Days & Car Speed")
plt.show()


# <b>Q. No. 2</b> Now to above car data apply some string formats  like line style example green dotted line, marker shape like +, change markersize, markerface color etc.

# In[19]:


import matplotlib.pyplot as plt #Importing the required library

Days = [1,2,3,4,5,6,7,8]
Speed = [60,62,61,58,56,57,46,63]

plt.figure(figsize=[8,6])
plt.plot(Days, Speed, color = 'Red', linestyle = 'dotted', linewidth = 3.5, marker = 'D', ms = 10, mfc = 'y', mec = 'b' )
# ms for marker size; mfc for marker face color; mec for border color
plt.xlabel("Days")
plt.ylabel("Speed")
plt.title("Days & Car Speed")
plt.show()


# <b>Q. No. 3 </b> Plot Axes Labels, Chart title, Legend, Grid in Car minimum, Maximum and average speed in 8 days.
# - days=[1,2,3,4,5,6,7,8]
# - max_speed=[80,91,92,88,77,79,76,75]
# - min_speed=[42,43,40,42,33,36,34,35]
# - avg_speed=[46,58,57,56,40,42,41,36]

# In[20]:


days=[1,2,3,4,5,6,7,8]
max_speed=[80,91,92,88,77,79,76,75]
min_speed=[42,43,40,42,33,36,34,35]
avg_speed=[46,58,57,56,40,42,41,36]

plt.figure(figsize=[10,6])
plt.plot(days, max_speed, color = 'b', linestyle = 'dotted', linewidth = 4.0, marker = 'D', ms =10, mfc = 'y', mec = 'r')
plt.xlabel("Day")
plt.ylabel("Maximum Speed")
plt.title("Day wise maximum speed of car")
plt.grid()
plt.show()

plt.figure(figsize=[10,6])
plt.plot(days, min_speed, color = 'r', linestyle='dotted', linewidth = 4.0, marker = "D", ms=10, mfc='w', mec='b')
plt.xlabel("Day")
plt.ylabel("Minimum Speed")
plt.title("Day wise minimum speed of the car")
plt.grid()
plt.show()

plt.figure(figsize=[10,6])
plt.plot(days, avg_speed, color='g', linestyle='dotted', linewidth=4.0, marker='D', ms=10, mfc='y', mec='r')
plt.xlabel("Day")
plt.ylabel("Average Speed")
plt.title("Day wise average speed of the car")
plt.grid()
plt.show()


# <b>Q. No. 4 </b> Plot Simple bar chart showing popularity of Programming Languages.
# - Languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# - Popularity = [56, 39, 34, 34, 29]
# - Security = [44 ,36 ,55, 50, 42]
# 
# Plot Multiple Bars showing Popularity and Security of major Programming Languages. Also Create Horizontal bar chart using barh function.

# In[3]:


Languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
Popularity = [56, 39, 34, 34, 29]
Security = [44 ,36 ,55, 50, 42]

plt.subplot(2,1,1)
plt.bar(Languages, Popularity, width=0.5, color='r', align='center')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of major programming languages")
plt.show()

plt.subplot(2,1,2)
plt.bar(Languages, Security, width=0.5, color='b', align='center')
plt.xlabel("Languages")
plt.ylabel("Security")
plt.title("Security of major programming languages")
plt.show()


# In[8]:


#Horizontal plot

plt.subplot(2,1,1)
plt.barh(Languages, Popularity, align='center', color='b')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of major programming languages")
plt.show()

plt.subplot(2,1,2)
plt.barh(Languages, Security, align='center', color='r')
plt.xlabel("Security")
plt.ylabel("Languages")
plt.title("Security of major programming languages")
plt.show()


# <b>Q. No. 5 </b> Plot Histogram, We have a sample data of Students marks of various Students, we will try to plot number of Students by marks range and try to figure out how many Students are average, below-average and Excellent.
# - Marks = [ 61,86,42,46,73,95,65,78,53,92,55,69,70,49,72,86,64]
# 
# Histogram showing Below Average, Average and Execellent distribution
# - 40-60: Below Average
# - 60-80: Average
# - 80-100: Excellent

# In[11]:


import numpy as np
Marks = np.array([ 61,86,42,46,73,95,65,78,53,92,55,69,70,49,72,86,64])

below_avg = Marks[np.logical_and(Marks>=40, Marks<60)]
avg = Marks[np.logical_and(Marks>=60, Marks<80)]
excellent = Marks[np.logical_and(Marks>=80, Marks<=100)]

plt.figure(figsize=[10,6])
plt.hist(Marks)
plt.show()

print("Students who scored below average marks are", below_avg.size)
print("Students who scored average marks are", avg.size)
print("Students who scored excellent marks are", excellent.size)


# <b>Q. No. 6</b> Titanic Data Set
#  
# Load the data file
# 
# (i) Create a pie chart presenting the male/female proportion 
# 
# (ii) Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[12]:


import pandas as pd

df = pd.read_csv(r"E:\Data Science\titanic_train.csv")

df.head()


# In[17]:


# Plotting pie chart to present male/female proportion
x = df.Sex.value_counts()
plt.figure(figsize=[6,6])
plt.pie(x, autopct = '%0.1f%%')
plt.legend(["Male","Female"])
plt.title("Male/Female Proportion")
plt.show()


# In[27]:


#Creating a scatterplot with the Fare paid and the Age, differ the plot color by gender

male = df[df['Sex']=='male']
male.Sex.value_counts()

female = df[df['Sex']=='female']
female.Sex.value_counts()

plt.figure(figsize=[15,8])
plt.scatter(male.Fare, male.Age, label = 'Male', marker='*')
plt.scatter(female.Fare, female.Age, label = 'Female', marker='^')
plt.legend()
plt.xlabel('Fare')
plt.ylabel('Age')
plt.title(' Fare paid and the Age')
plt.grid()
plt.show()


# In[ ]:




