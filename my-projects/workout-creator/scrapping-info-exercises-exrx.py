import cloudscraper # == requests that can bypass CloudFlare's anti-bot page
from bs4 import BeautifulSoup

# Which info you consider important?
# Get the info
# Second goal: store all the impotant info in a csv file

def get_html(url):
    scraper = cloudscraper.create_scraper()
    html_text = scraper.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)
    return soup


def get_info(soup):
    name = soup.find('h1').text
    
    classification = soup.find_all('td', {'width': '60%'})
    utility = classification[0].text
    mechanics = classification[1].text
    force = classification[2].text
    
    column = soup.find_all('div', {'class': 'col-sm-6'})
    muscles_name = column[1].find_all('ul')
    target = [x.text for x in muscles_name[0].find_all('li')]
    synergist = [x.text for x in muscles_name[1].find_all('li')]

    info = f'''
Name: {name}
Utility: {utility}
mechanics: {mechanics}
Force: {force}
Target: {target}
Synergist: {synergist}'''

    print(info)



def main():
    file_links = 'links-exercises-exrx.net.txt'
    csv_file = 'info-exercises.csv'
    ls = []
    with open(file_links, 'r') as links:
        for link in links:
            link = link.replace('\n','')
            # print(link)

            soup = get_html(link)
            csv_file = get_info(soup)
            
            
            




if __name__ == '__main__':
    main()