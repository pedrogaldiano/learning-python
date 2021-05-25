import cloudscraper # == requests that can bypass Cloudflare's anti-bot page
from bs4 import BeautifulSoup


# Get all the main muscles link
# Get all the sub links inside the main muscle link (a for loop will do the trick)
# First goal: Store all the links to the exercises in a txt file

def get_html(url):
    scraper = cloudscraper.create_scraper()
    html_text = scraper.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    return soup


def get_links_directory(soup):
    a_tags = soup.find_all('a')
    
    links = []
    for a_tag in a_tags:
        a_tag_href = a_tag['href']
        
        if not (a_tag_href[0] == '/' or \
            a_tag_href[0] == '.' or \
            'http' in a_tag_href or \
            '#' in a_tag_href or \
            'Search' in a_tag_href or \
            'Muscle' in a_tag_href or \
            'WorkoutMenu' in a_tag_href): 

            links.append(a_tag['href'])
    return links


def get_links_exercises(soup):
    links = []
    a_tags = soup.find_all('a')
    for a_tag in a_tags: 

        try:
            a_tag_href = a_tag['href']
            if a_tag_href[0] == '.' or a_tag_href[0] == 'h':
                if ('WeightExercises' in a_tag_href): #or \
                    # 'Stretches' in a_tag_href or \
                    # 'Aerobic' in a_tag_href or \
                    # 'Plyometrics' in a_tag_href or \
                    # 'Kettlebell' in a_tag_href):
    
                    a_tag_href = a_tag_href.replace('../../','https://exrx.net/') \
                        .replace('../','https://exrx.net/')
                    links.append(a_tag_href)
        except:
            continue
    return links


def main(): 
    filename = 'links-exercises-exrx.net.txt'
    url = 'https://www.exrx.net/'
    
    soup_dir = get_html(url + 'Lists/Directory/')
    links_dir = get_links_directory(soup_dir)
    
    for link_dir in links_dir: 
        soup_ex = get_html(url + 'Lists/' + link_dir)
        links_ex = get_links_exercises(soup_ex)
        
        for link_ex in links_ex:
            with open(filename, 'a') as exercises:
                exercises.write(link_ex)
                exercises.write('\n')
                
        
if __name__ == '__main__':
    main()