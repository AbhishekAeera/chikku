# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:24:06 2023

@author: Abhi
"""

import pandas as pd #Inputing file (eg, pd.read_csv), Data-processing
import matplotlib.pyplot as plt #Visualisation

#Reading the dataset by dataframe as 'df':
df = pd.read_csv("airwaays2.csv") #Reading the file

#Generates lineplot for Dataframe
def plot_airline_incidents(df):
    ''' In summary, this code is used to create a line plot that visualizes the number of airline incidents and fatal incidents over time. 
       The line plot is interactive, allowing users to zoom in and out of the plot to gain more insight into the data.'''
    
    # Define a new figure size
    plt.figure(figsize=(30,10))
   
    # Plot the incidents
    plt.plot(df["airline"], df["incidents"], marker="o", label="Incidents")
    
    # Plot the fatal incidents
    plt.plot(df["airline"], df["fatal accidents"], marker="o", label="Fatal Accidents")

#Set title and labels
    plt.title("Airline Incidents")
    plt.xlabel("Airline")
    plt.ylabel("Number of Incidents")
# Display the plot
    plt.show()

# Assuming 'df' is your dataframe    
plot_airline_incidents(df)

#Generates barplot for Dataframe
def plot_airline_incidents(df):
    ''' In this code, a bar plot is generated to visualize the number of incidents 
       and fatal incidents for different airlines.'''

    '''This line sets the width of the bars. The value 0.35 is chosen so that there is sufficient space between the bars for readability.'''
    bar_width = 0.35
    '''This line creates a list of indices, from 0 to the length of the dataframe df (which represents the number of airlines). This will be used as the x-coordinate for the bars.'''
    index = range(len(df))
    
    # Plot the incidents
    plt.bar(index, df["incidents"], bar_width, label="Incidents", color="b")
    '''This line creates a bar plot for the number of incidents for each airline. 
    The index list is used as the x-coordinates, df["incidents"] is used as the heights of the bars, bar_width is the width of the bars, 
    the label for the legend is set to "Incidents", and the color of the bars is set to blue.'''
   
    # Plot the fatal incidents
    plt.bar([i + bar_width for i in index], df["fatal accidents"], bar_width, label="Fatal Accidents", color="r")

    plt.xticks([i + bar_width/2 for i in
                index], df["airline"], rotation=90)
    # Add a legend
    plt.legend()
    #Set title and labels
    plt.title("Airline Incidents")
    plt.xlabel("Airline")
    plt.ylabel("Number of Incidents")
    # Display the plot
    plt.show()

# Assuming 'df' is your dataframe
plot_airline_incidents(df)

#Defining a function 'scatterPlot' to generate a scatter plot with specified data, x and y features, title, x and y axis labels, and marker position.
def plot_airline_incidents(df):
    fig, ax = plt.subplots(figsize=(20,10))

    ax.scatter(df["airline"], df["incidents"], label="Incidents")
    ax.scatter(df["airline"], df["fatal accidents"], label="Fatal accidents")

    ax.legend()
    ax.set_title("Airline Incidents")
    ax.set_xlabel("Airline")
    ax.set_ylabel("Number of Incidents")
    plt.show()

# Assuming 'df' is your dataframe
plot_airline_incidents(df)


