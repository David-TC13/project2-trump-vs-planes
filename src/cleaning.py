# Cleaning process
def cl_colm (df_suicide):
    df_suicide.drop(axis=1, columns=['suicides/100k pop', 'country-year', 'HDI for year',' gdp_for_year ($) ', 'gdp_per_capita ($)'], inplace = True)
    return df_suicide

def cl_country_year_null(df_suicide):
    df_suicide_uk=df_suicide[df_suicide.country =='United Kingdom']
    df_suicide_uk = df_suicide_uk[df_suicide_uk['suicides_no'].notna()]
    df_suicide_uk = df_suicide_uk[df_suicide_uk.year>2004]
    return df_suicide_uk

def cl_year(df_suicide_uk):
    df_suicide_uk = df_suicide_uk[df_suicide_uk.year>2004]
    return df_suicide_uk

