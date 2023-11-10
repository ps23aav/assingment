# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_1(df):
    # Visualisation 1-Line chart
    # Select a few countries for visualization, replace 'Country1',
    #'Country2'... with actual country names
    countries_to_visualize = ['India', 'United Kingdom', 'United States']

    # Filter the dataframe to include only the selected countries
    filtered_df = df[df['Country Name'].isin(countries_to_visualize)]

    # Set the index to 'Country Name' to facilitate plotting
    filtered_df.set_index('Country Name', inplace=True)

    # Select the years columns for plotting
    # This selects the last 7 columns which are the years
    years = filtered_df.columns[-7:]

    # Plotting
    plt.figure(figsize=(10, 6))

    for country in countries_to_visualize:
        plt.plot(years, filtered_df.loc[country,
                 years], marker='o', label=country)

    plt.title('GDP Growth Rate from 2016 to 2022')
    plt.xlabel('Year')
    plt.ylabel('GDP Growth Rate (%)')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_2(df):
    # Visualisation 2-Bar chart
    # Manually define regions for a set of countries
    regions = {
        'Americas': ['Brazil', 'United States', 'Canada'],
        'Europe': ['Germany', 'France', 'United Kingdom'],
        'Africa': ['Nigeria', 'Egypt', 'South Africa'],
        'Asia': ['China', 'India', 'Japan']
    }

    # Create a new column for region by mapping the country name to its region
    df['Region'] = df['Country Name'].apply(lambda x: next(
        (region for region, countries in regions.items() if x in countries)
        ,None))

    # Filter out rows where the region is None (i.e., the country wasn't
    # listed in our regions dictionary)
    df = df[df['Region'].notna()]

    # Group by region and calculate the average GDP growth rate for the year
    # 2019
    average_growth_by_region = df.groupby('Region')['2019'].mean()

    # Plotting the bar chart
    plt.figure(figsize=(10, 6))

    # Plotting each region's average growth rate for 2019
    plt.bar(average_growth_by_region.index, average_growth_by_region.values,
            color=['blue', 'green', 'red', 'purple'])

    plt.title('Average GDP Growth Rate by Region for 2019')
    plt.xlabel('Region')
    plt.ylabel('Average GDP Growth Rate (%)')
    plt.xticks(rotation=45)  # Rotate region names for better readability
    plt.grid(axis='y')  # Add a grid on the y-axis for easier comparison

    plt.show()


def plot_3(df):
    # Visualisation 3-Histogram
    # Select the GDP growth rates for the year 2019
    # Drop NaN values to avoid errors in the histogram
    growth_rates_2019 = df['2019'].dropna()

    # Plotting the histogram
    plt.figure(figsize=(10, 6))

    # Create the histogram with a suitable number of bins
    plt.hist(growth_rates_2019, bins=20, color='skyblue', edgecolor='black')

    plt.title('Distribution of GDP Growth Rates for 2019')
    plt.xlabel('GDP Growth Rate (%)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)  # Add a grid for better readability

    plt.show()


df = pd.read_csv('GDP.csv', skiprows=4)
df = df.dropna()
print(df.head(20))

plot_1(df)
plot_2(df)
plot_3(df)
