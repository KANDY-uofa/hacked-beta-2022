# BeautifulSoup for web scraping 
import requests
from bs4 import BeautifulSoup
import re

def num_cities(url):
    """
    This function returns the list of cities under the "Traffic by City" tab.
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
    """
    This function modifies the format of the city list so that it can be incorprated in hyperlink.
    It returns a list of the modified formats.
    """
    
    hyper_city_list = []
    
    # modify the format
    for city in list_cities:
        city = city.replace(" ", "_").lower()
        if "_traffic" in city:
            city = city.replace("_traffic","_1_archived_reports")
        hyper_city_list.append(city)

    return hyper_city_list

def get_archived_link(link_of_desired_city):
    """
    This function gets the link of the 2022 incident archives of the specified city. 
    """
    full_link = "https://www.navbug.com/alberta/{}.htm".format(link_of_desired_city)
    return full_link

def get_archived_titles(full_link):
    """
    This function returns the titles of the archived posts.
    """
    url = full_link
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")
    # all posts have "Incident Archives"
    post_titles = soup.find_all(string = re.compile("Incident Archives"))
    archived_post_list = []
    for title in post_titles:
        archived_post_list.append(title.text)
    return archived_post_list

def trim_archives(archived_post_list):
    """
    This function removes the posts that are not of concern (prior to 2021).
    """
    list2021 = []
    list2022 = []

    for post in archived_post_list:
        if "2021" in post:
            list2021.append(post)
        elif "2022" in post:
            list2022.append(post)
        else:
            continue
    return list2021, list2022

def get_archive_link(archive_list, year, city):
    """
    This function returns the list of links to archived reports.
    """

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    month_list = []
    for title in archive_list:
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

    date_list = []
    for i in range(len(month_list)):
        date_list.append(str(year) + month_list[i])

    link_list = []
    for date in date_list:                              # to change the area, change "edmonton"
        link_list.append("https://www.navbug.com/alberta/{}/archives/{}.htm".format(city,date))
    return link_list

def num_posts(link_list):
    """
    This function returns the number of posts in one year.
    """
    num_posts = 0
    for link in link_list:
        result = requests.get(link)
        soup = BeautifulSoup(result.text, "lxml")
        post_titles = soup.find_all("span",{"class":"listarticle_title"})
        post_list = []
        for post in post_titles:
            post_list.append(post.text)
        num_posts += len(post_list)
    return num_posts

def list_options(list_cities):
    """
    This function shows the list of city options that you can input in "get_archived_link" function.
    """
    list_of_cities = []
    for city in list_cities:
        list_of_cities.append(city.lower().replace(" ","_").replace("_traffic",""))
    
    return list_of_cities

def scrape_main(city):
    list_cities = num_cities("https://www.navbug.com/alberta/calgary_traffic.htm")
    formatted_list = format_list(list_cities)
    print(list_options(list_cities))
    print(formatted_list)
    archive_list = get_archived_link(formatted_list[5]) #[1] is the edmonton
    archived_titles = get_archived_titles(archive_list)
    list2021, list2022 = trim_archives(archived_titles)
    list_of_archived_link2021 = get_archive_link(list2021, 2021, city)
    list_of_archived_link2022 = get_archive_link(list2022, 2022, city)
    num2021 = num_posts(list_of_archived_link2021)
    num2022 = num_posts(list_of_archived_link2022)
    print('2021:', num2021)
    print('2022:', num2022)

if __name__ == "__main__":
    scrape_main("medicine_hat")





