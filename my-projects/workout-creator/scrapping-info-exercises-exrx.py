import cloudscraper # == requests that can bypass CloudFlare's anti-bot page
from bs4 import BeautifulSoup
import sqlite3

# Which info you consider important?
# Get the info
# Second goal: store all the impotant info in a csv file

# Use the Beautifulsoup to get the html
def get_html(url):
    scraper = cloudscraper.create_scraper()
    html_text = scraper.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)
    return soup


# Web Scrapping - Some info doesn't match any criteria (20/1421)
# I wrapped everything in a try
def get_info(soup):
    try:
        name = soup.find('h1').text
        
        classification = soup.find_all('td', {'width': '60%'})
        # print(classification)
        utility = classification[0].text
        mechanic = classification[1].text
        force = classification[2].text
        
        column = soup.find_all('div', {'class': 'col-sm-6'})
        muscles_name = column[1].find_all('ul')
        
        target = [x.text for x in muscles_name[0].find_all('li')]
        target = str(target).replace('[','').replace(']', '').replace("'",'')
        
        synergist = [x.text for x in muscles_name[1].find_all('li')]
        synergist = str(synergist).replace('[','').replace(']', '').replace("'",'')
    
        info = (name, utility, mechanic, force, target, synergist)
        return info
    
    except:
        return


# Open the links file, acess each one of them 
# and then store that info in a sqlite database
def main():
    file_links = 'links-exercises-exrx.net.txt'
    conn = sqlite3.connect('table-all.db')
    c = conn.cursor()

    with open(file_links, 'r') as links:
        for link in links:
            link = link.replace('\n','')

            soup = get_html(link)
            info = get_info(soup)

            try:
                c.execute("INSERT INTO exercises VALUES (?,?,?,?,?,?)", info)
                conn.commit()
            except:
                with open('errors.txt', 'a') as errors:
                    errors.write(link + '\n')
                continue
    conn.close()
    
    
# # After all done, just check if everything is worked
#     c.execute('SELECT * FROM exercises')
#     counter = 0
#     for item in c.fetchall():
#         counter += 1
#         print(item)
#         if counter > 1400:
#             print(f'\n\nCounter is {counter}')
#     conn.close()


if __name__ == '__main__':
    main()