from app import file, soup
import os
import requests


def main():
    directory = 'data/'
    extension = '.htm'
    pids = [
        '1572142',  # Adelard Charest
        '1572141',  # Alma Tanguay
        '1713616',  # Joseph Charest
        '1713617',  # Martine Lebrun
        '1196958',  # Jean-Baptiste-Celestin Tanguay
        '1196957',  # Adele Bedard
        '26378',  # Robert-Mathieu, Choret
        '26379'  # Sebastienne, Veillon
    ]
    get_files(pids)
    persons = []

    for p in range(0, len(pids)):
        # Read
        file_ = f'{directory}{pids[p]}{extension}'
        string = file.read(file_)

        # Extract data
        soup_ = soup.make_soup(string)
        persons.append(
            {
                'pid': soup.find(soup_, 'td', {'class': 'tdlb', 'style': 'width:245px;'})[0],
                'firstName': soup.find(soup_, 'td', {'class': 'tdlb'}, 'strong')[0],
                'lastName': soup.find(soup_, 'td', {'class': 'tdl', 'style': 'vertical-align:top;'}, 'b')[0],
                'gender': soup.find(soup_, 'td', {'class': 'tdl'})[1][0],
                'partner': soup.find(soup_, 'td', {'class': 'tdlb', 'style': 'width:245px;'})[1]
            }
        )
        soup_.clear()

    for person in persons:
        print(person)


def get_file(pid, file_, url='https://www.nosorigines.qc.ca/GenealogieQuebec.aspx?pid=', encoding='windows-1252'):
    # Crawl
    response = requests.get(f'{url}{pid}')
    string = response.content.decode(encoding)

    # Write
    file.write(string, file_)


def get_files(pids, directory='data/', extension='.htm'):
    for pid in pids:
        file_ = f'{directory}{pid}{extension}'

        if not os.path.isfile(file_):
            get_file(pid, file_)


if __name__ == '__main__':
    main()
