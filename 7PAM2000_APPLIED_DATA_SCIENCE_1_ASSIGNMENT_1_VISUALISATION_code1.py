# -*- coding: utf-8 -*-
"""
7PAM2000_APPLIED_DATA_SCIENCE_1_ASSIGNMENT_1_VISUALISATION

@author: Pedro Neto
"""

#Importing Pandas and Matplotlib.pyplot Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Creating Functions
def lineplot_countries(iso0, iso1, iso2, iso3, iso4):
    """
    This function was created to produce a line plot of COVID-19 cases by time
    
    Args:
        iso0 (str): select a country with the iso_code
        iso1 (str): select a country with the iso_code
        iso2 (str): select a country with the iso_code
        iso3 (str): select a country with the iso_code
        iso4 (str): select a country with the iso_code
        
    Return:
        Save and show a line plot of COVID-19 cases by time
    """
    fig, ax = plt.subplots(dpi=240)
    
    ax.plot(df[df.iso_code == iso0]['date'], df[df.iso_code == iso0]\
            ['total_cases'],label='{}'.format(iso0), linewidth=3)
    ax.plot(df[df.iso_code == iso1]['date'], df[df.iso_code == iso1]\
            ['total_cases'], label='{}'.format(iso1), linewidth=3)
    ax.plot(df[df.iso_code == iso2]['date'], df[df.iso_code == iso2]\
            ['total_cases'], label='{}'.format(iso2), linewidth=3)
    ax.plot(df[df.iso_code == iso3]['date'], df[df.iso_code == iso3]\
            ['total_cases'], label='{}'.format(iso3), linewidth=3)
    ax.plot(df[df.iso_code == iso4]['date'], df[df.iso_code == iso4]\
            ['total_cases'], label='{}'.format(iso4), linewidth=3)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend()

    plt.title('{}, {}, {}, {}, {} Covid Cases'.format(iso0, iso1, iso2,
                                                      iso3, iso4))
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.ylabel('Cases')

    plt.savefig('plot1', dpi=300)
    
    return plt.tight_layout();

def barhplot_countries(iso0, iso1, iso2, iso3, iso4):
    """
    This function was created to produce a horizontal bar chart of COVID-19 
    deaths by countries
    
    Args:
        iso0 (str): select a country with the iso_code
        iso1 (str): select a country with the iso_code
        iso2 (str): select a country with the iso_code
        iso3 (str): select a country with the iso_code
        iso4 (str): select a country with the iso_code
        
    Return:
        Save and show a horizontal bar chart of COVID-19 deaths by countries
    """

    bar_colors = ['lightsalmon', 'thistle','khaki',
                  'peachpuff','tan']

    fig, ax = plt.subplots(dpi=240)

    ax.barh(df_date[df_date.iso_code==iso0]['iso_code'],
         df_date[df_date.iso_code==iso0]['total_deaths'],
         color=bar_colors[0])
    ax.barh(df_date[df_date.iso_code==iso1]['iso_code'],
         df_date[df_date.iso_code==iso1]['total_deaths'],
         color=bar_colors[1])
    ax.barh(df_date[df_date.iso_code==iso2]['iso_code'],
         df_date[df_date.iso_code==iso2]['total_deaths'],
         color=bar_colors[2])
    ax.barh(df_date[df_date.iso_code==iso3]['iso_code'],
         df_date[df_date.iso_code==iso3]['total_deaths'],
         color=bar_colors[3])
    ax.barh(df_date[df_date.iso_code==iso4]['iso_code'],
         df_date[df_date.iso_code==iso4]['total_deaths'],
         color=bar_colors[4])

    plt.title('Covid Deaths by Countries')
    plt.xlabel('Deaths')
    plt.ylabel('Contries')

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.savefig('plot2', dpi=300)
    return plt.tight_layout();

def boxplot_continent(cont0, cont1, cont2):
    """
    This function was created to produce three boxplots of people fully
    vaccinated aginst COVID-19 by continents
    
    Args:
        cont0 (str): select a country with the continent name
        cont1 (str): select a country with the continent name
        cont2 (str): select a country with the continent name
        
    Return:
        Save and show three boxplots of people fully vaccinated aginst 
        COVID-19 by continents
    """

    fig, ax = plt.subplots(3,1, figsize=(10,8), dpi=240)

    df_date[df_date['continent']==cont0]['people_vaccinated/population'].plot(
        kind='box', vert=False,ax=ax[0])
    df_date[df_date['continent']==cont1]['people_vaccinated/population'].plot(
        kind='box', vert=False, ax=ax[1])
    df_date[df_date['continent']==cont2]['people_vaccinated/population'].plot(
        kind='box', vert=False, ax=ax[2])

    ax[0].set_xticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['left'].set_visible(False)
    ax[0].spines['top'].set_visible(False)
    ax[0].set_yticks(ticks=[])
    ax[0].set_ylabel('{}'.format(cont0))
    ax[0].set_title(
        'Percentual of People Fully Vaccinated per population by Continent')
    # ax[0].set_xticks(ticks=[])

    ax[1].set_xticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['left'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].set_yticks(ticks=[])
    ax[1].set_ylabel('{}'.format(cont1))
    # ax[1].set_xticks(ticks=[])

    ax[2].set_xticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    ax[2].spines['right'].set_visible(False)
    ax[2].spines['left'].set_visible(False)
    ax[2].spines['top'].set_visible(False)
    ax[2].set_yticks(ticks=[])
    ax[2].set_xlabel('Percentual of People Vaccinated per Population')
    ax[2].set_ylabel('{}'.format(cont2))

    # plt.title('Continent - People Fully Vaccinated per population')
    # plt.ylabel('Continent')
    plt.xlabel('Percentage of People Vaccinated per Population')

    plt.savefig('plot3', dpi=300)
    return plt.tight_layout();

#Assigning Database path to variable database_path
database_path = ('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
#Importing data
data = pd.read_csv(database_path)
#Creating a backup
df = data.copy()

#Showing DataFrame size 
print(f'Rows: {df.shape[0]}') 
print(f'Variables {df.shape[1]}')
#Showing Dataframe types
print(df.dtypes)

#Converting 'date' into a pandas datetime
df.date = pd.to_datetime(df.date)

#Creating a dataframe with a especific date
date = '2022-11-01'
df_date = (df.loc[df.date == date])\
            .sort_values('total_cases', ascending=False)\
            [df.iso_code.str.startswith('OWID') == False]

#Creating a column with the percentual of people vaccinated per population
df_date['people_vaccinated/population'] = df_date['people_fully_vaccinated']\
                                                    /df_date['population']

#Calling plot functions
lineplot_countries('BRA', 'DEU', 'FRA', 'IND', 'USA')
barhplot_countries('USA', 'BRA', 'IND', 'RUS', 'MEX')
boxplot_continent('Europe', 'North America', 'Africa')