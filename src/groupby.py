def group_suici_age (df_suicide_uk):
    df_suicide_ages=df_suicide_uk[['year','age','generation','suicides_no']].groupby(by=['age', 'year']).agg({"suicides_no":"sum"})
    return df_suicide_ages

def group_season_epi (df_loveisland_until_2020):
    df_distr_epi=df_loveisland_until_2020[['Year','Month','Season','Episode']].groupby(by=['Season','Year']).agg({'Episode':'count'})
    return df_distr_epi