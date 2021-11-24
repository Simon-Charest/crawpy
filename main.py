from app import file, soup
import os
import requests


def main():
    pid = '26378'
    url = f'https://www.nosorigines.qc.ca/GenealogieQuebec.aspx?pid={pid}'
    file_ = f'data/{pid}.htm'
    encoding = 'windows-1252'

    if not os.path.isfile(file_):
        # Crawl
        response = requests.get(url)
        string = response.content.decode(encoding)

        # Write
        file.write(string, file_)

    # Read
    string = file.read(file_)

    first_names = []
    last_names = []
    genders = []
    persons = []

    soup_ = soup.make_soup(string)

    # Fetch values
    pids = soup.find(soup_, 'td', {'class': 'tdlb', 'style': 'width:245px;'})
    values = soup.find(soup_, 'td', {'class': 'tdl'})

    # Current person
    first_names += soup.find(soup_, 'td', {'class': 'tdlb'}, 'strong')
    last_names += soup.find(soup_, 'td', {'class': 'tdl', 'style': 'vertical-align:top;'}, 'b')
    genders += values[1][0]

    # Partner
    first_names += soup.find(soup_, 'td', {'class': 'tdlb'}, 'a')
    last_names += soup.find(soup_, 'td', {'class': 'tdl'}, 'a')
    genders += values[10][0]

    soup_.clear()

    # Organize values
    for x in range(0, len(pids)):
        persons += [{
            'pid': pids[x],
            'firstName': first_names[x],
            'lastName': last_names[x],
            'gender': genders[x],
            'partner': pids[1 if x == 0 else 0]
        }]

    for person in persons:
        print(person)


if __name__ == '__main__':
    main()
