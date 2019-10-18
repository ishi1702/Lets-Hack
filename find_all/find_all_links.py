from bs4 import BeautifulSoup, SoupStrainer
import requests
import validators


def get_links_from_url(url):
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, features="html.parser")

    for link in soup.find_all('a'):
        print(link.get('href'))


def get_url_from_user():
    url = input("Please input the URL to show all its links: ")
    while validators.url(url) is not True:
        url = input("Please input a valid URL: ")
    return url


if __name__ == '__main__':
    url = get_url_from_user()
    get_links_from_url(url)
