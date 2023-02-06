import pandas as pd
def dictionary(lst_seasons,lst_episodes,year,month):
    """Creates a new dictionary with lists as values"""
    love_island_dict={
    'Season': lst_seasons,
    'Episode': lst_episodes,
    "Year": year,
    "Month": month
    }
    return love_island_dict

def dfloveisland (love_island_dict):
    """Creates and clears a df from a dictionary of keys as titles and values lists"""
    df_loveisland = pd.DataFrame.from_dict(love_island_dict)
    df_loveisland.Year= df_loveisland.Year.astype("int")
    df_loveisland.Season= df_loveisland.Season.astype("int")
    df_loveisland.Episode= df_loveisland.Episode.astype("int")
    df_loveisland_until_2020 = df_loveisland[df_loveisland.Year <2020]
    return df_loveisland_until_2020
