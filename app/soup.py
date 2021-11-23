from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import lxml
import urllib3
import xlsxwriter


def find(soup, parent_name, attrs=None, child_name=None):
    values = []
    parents = soup.find_all(parent_name, attrs)

    for parent in parents:
        if child_name:
            children = parent.find_all(child_name)

            for child in children:
                values.append(child.text)

        else:
            values.append(parent.text)

    return values


def get_data(url, method='GET'):
    http = urllib3.PoolManager()
    response = http.request(method, url)

    return response.data


def make_soup(markup, features='lxml'):
    return BeautifulSoup(markup, features)
