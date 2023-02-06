import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import warnings

def join_df(df_suicide_uk, df_loveisland_until_2020):
    
    """It creates a new df joining two by the year column, which is the common element,set as index"""
    df_loveisland_until_2020= df_loveisland_until_2020.drop(columns=['Month'])
    df_join= df_suicide_uk.set_index('year').join(df_loveisland_until_2020.set_index('Year'))
    return df_join

def r_index(df_join): 
    
    """ Redefine the index, creating a new column called 'year' """
    df_join['year'] = df_join.index
    df_join = df_join.reset_index(level=0)
    return df_join

    
def year_suic_season(df_join):
    """Creates a combination of a barplot and a lineplot"""
    matplotlib.rc_file_defaults()
    ax1 = sns.set_style(style=None, rc=None )
    fig, ax1 = plt.subplots(figsize=(8,4))
    sns.lineplot(data = df_join['suicides_no'], marker='o', sort = False, ax=ax1)
    ax2 = ax1.twinx()
    sns.barplot(data = df_join, x='year', y='Episode', alpha=0.5, ax=ax2, ci=None)
    plt.title('Suicides no. vs. Episodes through the years')
    return fig


