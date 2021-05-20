# import requests
import cloudscraper # == requests + bypass Cloudflare's anti-bot page
from bs4 import BeautifulSoup
URL_CONST = 'https://www.exrx.net/'

# Get all the main muscles link
# Get all the sub links inside the main muscle link (a for loop will do the trick)
# First goal: Store all the links to the exercises in a txt

def get_html(url_add):
    url = URL_CONST + url_add
    print(url)
    
    scraper = cloudscraper.create_scraper()
    html_text = scraper.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    return soup
    
def get_links(soup):
    a_tags = soup.find_all('a')
    
    for a_tag in a_tags:
        a_tag_href = a_tag['href']
        
        check = [a_tag_href[0] == '/',
                  a_tag_href[0] == '.',
                  'http' in a_tag_href,
                  '#' in a_tag_href,
                  'Search' in a_tag_href, 
                  'Muscle' in a_tag_href, 
                  'WorkoutMenu' in a_tag_hre]: 
                        
               print('https://www.exrx.net/Lists/' + a_tag['href'])
        
    

def main():
    
    soup = get_html('Lists/Directory/')
    get_links(soup)
    
    # #fix the urls (remove /Directory and add /whatever)
    # for link in links:
    #     sub_links = get_links(link)
        
if __name__ == '__main__':
    main()
    
    
    
    
    