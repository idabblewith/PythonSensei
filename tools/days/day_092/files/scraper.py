import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    # Send an HTTP request and get the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    return soup.prettify()
