from bs4 import BeautifulSoup
import requests

def extrc(url):
    
    """Applies BeatifulSoup to a url, creating a parser instance able to parse invalid markup"""
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup

def clearance_date(love_island_date):
    
    """Clears up the data obtained looking for the date"""
    lst_date=[ i.getText().replace(',', '').replace('\n', ' ').split() for i in love_island_date]
    for i in lst_date:
        i.pop()
    return lst_date

def def_year(lst_date):
    
    """Creates a list of the years"""
    year =[i[2] for i in lst_date]
    return year

def def_month(lst_date):
    
    """Creates a list of the months"""
    month =[i[0] for i in lst_date]
    return month