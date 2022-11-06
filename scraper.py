# BeautifulSoup for web scraping 
import requests
from bs4 import BeautifulSoup
import re

def num_cities(url):
    """
    This function returns the list of cities and an integer number of cities that the website
    displays under the "Traffic by City" tab.
    """
    # website content
    result = requests.get(url)

    # parse through website content
    soup = BeautifulSoup(result.text, "lxml")

    # find the length of the list of cities
    # scrape the list of cities from website
    possible_cities = soup.find_all("ul",{"class":"sidebar-list"})
    list_cities = []  # initialize the list of cities

    # split a single string of cities
    for city in possible_cities:  
        list_cities.append(city.text.split("\n"))

    # there are multiple lists with the same tag --> scrape the desired one
    list_cities = list_cities[0]

    # trim the list
    while '' in list_cities:
        list_cities.remove('')

    return list_cities


def format_list(list_cities):
    '''
    This function modifies the format of the city list so that it can be incorprated in hyperlink.
    '''
    
    hyper_city_list = []
    
    # modify the format
    for city in list_cities:
        city = city.replace(" ", "_").lower()
        if "_traffic" in city:
            city = city.replace("_traffic","_1_archived_reports")
        hyper_city_list.append(city)

    return hyper_city_list


def click_city(hyper_city_list):
    """
    This function returns the hyperlink for the specified city.
    """
    city_link_list = []
    for city in hyper_city:
        city_link_list.append("https://www.navbug.com/alberta/{}.htm".format(city))
    return city_link_list

def archived_hyperlist(url):
    """
    This function returns a list of hyperlinks for the archived data for one city.
    """
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    post_titles = soup.find_all(string = re.compile("Incident Archives"))
    
    year_list = []
    for title in post_titles:
        year = re.findall(r"[0-9]{4,4}",title)
        year_list.append(year)

    new_year_list = []
    for i in range(len(year_list)):
        new_year_list.append(year_list[i][0])  # returns a list of years in string form

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    month_list = []
    for title in post_titles:
        if months[0] in title:
            month_list.append("01")
        elif months[1] in title:
            month_list.append("02")
        elif months[2] in title:
            month_list.append("03")
        elif months[3] in title:
            month_list.append("04")
        elif months[4] in title:
            month_list.append("05")
        elif months[5] in title:
            month_list.append("06")
        elif months[6] in title:
            month_list.append("07")
        elif months[7] in title:
            month_list.append("08")
        elif months[8] in title:
            month_list.append("09")
        elif months[9] in title:
            month_list.append("10") 
        elif months[10] in title:
            month_list.append("11")
        elif months[11] in title:
            month_list.append("12")

    assert len(new_year_list) == len(month_list)
    
    date_list = []

    for i in range(len(new_year_list)):
        date = "".join(new_year_list[i] + month_list[i])
        date_list.append(date)

    hyper_list = []
    
    for date in date_list:
        hyper_list.append("https://www.navbug.com/alberta/edmonton_traffic/archives/{}.htm".format(date))
    return hyper_list

def get_news_num(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    post_titles = soup.find_all("span",{"class":"listarticle_title"})
    
    new_titles = []
    for title in post_titles:
        new_titles.append(title.text)
    news_num = len(new_titles)
    
    return news_num
"""
if __name__ == "__main__":
   list_cities = num_cities("https://www.navbug.com/alberta/calgary_traffic.htm")
   print(list_cities)


    # list_cities,  number_of_cities = num_cities("https://www.navbug.com/alberta/calgary_traffic.htm")
    # hyper_city_list = format_list(list_cities)
    # for city in hyper_city_list:
    #       link = click_city(city)
    #       hyper_list = archived_hyperlist(link)
    #       for link in hyper_list:
    #           get_news_num
    #               
    #           
    
    list_cities, number_of_cities = num_cities("https://www.navbug.com/alberta/calgary_traffic.htm")
    hyper_city_list = format_list(list_cities)
    for city in hyper_city_list:
        link = click_city(city)
        hyper_list = archived_hyperlist(link)
        for link in hyper_list:
            print(link)
            num = get_news_num(link)
            print(num)
"""



