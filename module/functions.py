from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary


# Functions

def get_url(search_term):
    """
    Generate a url from search term
    """
    clean_search_term = search_term.replace(' ', '+')

    # add term query to url
    url = f'https://www.amazon.com/s?k={clean_search_term}&language=en_US&ref=nb_sb_noss_2'

    # add page to query
    url += '&page{}'

    return url


def extract_record(item):
    """
    Extract and return data from a single record
    """

    # Getting description and url

    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    try:
        """ Not all the items have the price on it """
        # Price
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return

    try:
        # Rank and rating
        rating = item.i.text
        review_count = item.find(
            'span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url)

    return result
