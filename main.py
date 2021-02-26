import csv
import chromedriver_binary
from bs4 import BeautifulSoup
from selenium import webdriver
from module.functions import get_url, extract_record


def main(search_term):
    """
    Run main program
    """
    # Start the webdriver
    """Important to configure your web driver"""
    driver = webdriver.Chrome()

    # Getting a list for the records
    records = []

    url = get_url(search_term)

    for page in range(1, 21):  # Page 20 is the maximun page you can get
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all(
            'div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    driver.close()

    # Save data on csv
    with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
        writer.writerows(records)


SEARCH_TERM = ''  # Add to this string your search term for the program


main(SEARCH_TERM)
