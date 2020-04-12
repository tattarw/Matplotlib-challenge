#!/usr/bin/env python
# coding: utf-8

# ## Observations and Insights 

# 

# In[142]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset

dataset = pd.merge(mouse_metadata, study_results, on ="Mouse ID" , how = "outer")
dataset.head()


# In[143]:


# Checking the number of mice in the DataFrame.

mice = dataset["Mouse ID"]
len(mice)


# In[144]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 


# In[145]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.

miceu = dataset["Mouse ID"].unique()


# In[146]:


# Checking the number of mice in the clean DataFrame.

len(miceu)


# ## Summary Statistics

# In[147]:


# Generate a summary statistics table of mean, median, variance, standard deviation, 
# and SEM of the tumor volume for each regimen

regimen = dataset.groupby(["Drug Regimen"])
rmean = regimen["Tumor Volume (mm3)"].mean()
rmedian = regimen["Tumor Volume (mm3)"].median()
rvar = regimen["Tumor Volume (mm3)"].var()
rsd =  regimen["Tumor Volume (mm3)"].std()
ssem = regimen["Tumor Volume (mm3)"].sem()
rcount = regimen["Mouse ID"].count()

summary_df = pd.DataFrame ({"Mean": rmean, "Median": rmedian, "Variance": rvar, "Standard Deviation": rsd, "SEM": ssem})


# In[148]:


rcount


# ## Bar Plots

# In[149]:


# Generate a bar plot showing the number of mice per time point for 
# each treatment throughout the course of the study using pandas. 

rcount = regimen["Mouse ID"].count()
rcount.plot(kind="bar", figsize=(10,5))

plt.title("Data Points Visual")
plt.xlabel("Drug Regimen")
plt.ylabel("Data Points")
plt.show()
plt.tight_layout()


# In[150]:


# Generate a bar plot showing the number of mice per time point 
# for each treatment throughout the course of the study using pyplot.

drugs = [230, 178, 178, 188, 186, 181, 161, 228, 181, 182]
x_axis = np.arange(len(rcount))
plt.bar(x_axis, drugs, color='b', alpha=1, align='center')
tick_locations = [value for value in x_axis]

plt.xticks(tick_locations, ['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol'],  rotation='vertical')
plt.xlim(-0.75, len(x_axis)-0.25)
plt.ylim(0, max(drugs)+10)
plt.title("Data Points Visual")
plt.xlabel("Drug Regimen")
plt.ylabel("Data Points")


# ## Pie Plots

# In[151]:


# Generate a pie plot showing the distribution of female versus male mice using panda

gender = pd.DataFrame(dataset.groupby(["Sex"]).count()).reset_index()
gender = gender [["Sex","Mouse ID"]]
gender = gender.rename(columns={"Mouse ID": "Count"})

plt.figure(figsize=(10,6))
pie = plt.subplot(121, aspect='equal')
gender.plot(kind='pie', y = "Count", ax=pie, autopct='%1.1f%%', 
 startangle=150, shadow=False, labels=gender['Sex'], legend = False, fontsize=15)


# In[152]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot

genders = ["Female","Male"]
percent = [49.4,50.6]
colors = ['orange', 'blue']
plt.pie(percent, labels=genders, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)


# ## Quartiles, Outliers and Boxplots

# In[153]:


# Calculate the final tumor volume of each mouse across four of the most promising 
# treatment regimens. 
# Calculate the IQR and quantitatively determine if there are any potential outliers. 

top4 = dataset[dataset["Drug Regimen"].isin(["Capomulin", "Ramicane", "Infubinol", "Ceftamin"])]
top4a = top4.sort_values(["Timepoint"], ascending=True)
top4b = top4a[["Drug Regimen", "Mouse ID", "Timepoint", "Tumor Volume (mm3)"]]


# In[167]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


# ## Line and Scatter Plots

# In[178]:


# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin

Tumor = dataset[dataset["Mouse ID"].isin(["s185"])]
Tumord = Tumor[["Mouse ID", "Timepoint", "Tumor Volume (mm3)"]]
Index = Tumord.reset_index()
line = Index[["Mouse ID", "Timepoint", "Tumor Volume (mm3)"]]
plot = line.plot.line()


# In[164]:


# Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin regimen

sp = dataset[dataset["Drug Regimen"].isin(["Capomulin"])]
sp_df = top4a[["Mouse ID","Weight (g)", "Tumor Volume (mm3)"]]
sp_plot = sp.reset_index()
sp_sorted = sp_plot.sort_values(["Weight (g)"], ascending=True)

group_w = sp_plot.groupby("Weight (g)")["Tumor Volume (mm3)"].mean()
sp_group = pd.DataFrame(group_w).reset_index()

sp_plot = sp_group.plot(kind='scatter', x='Weight (g)', y='Tumor Volume (mm3)', grid = True, figsize= (6,6))


# In[ ]:





# ## Correlation and Regression

# In[157]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen


# In[177]:


sp['Weight (g)'].corr(sp['Tumor Volume (mm3)'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




