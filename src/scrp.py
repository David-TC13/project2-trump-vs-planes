from bs4 import BeautifulSoup
import requests

def extrc(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup

def clearance_date(love_island_date):
    lst_date=[ i.getText().replace(',', '').replace('\n', ' ').split() for i in love_island_date]
    for i in lst_date:
        i.pop()
    return lst_date

def def_year(lst_date):
    year =[i[2] for i in lst_date]
    return year

def def_month(lst_date):
    month =[i[0] for i in lst_date]
    return month