from bs4 import BeautifulSoup
import requests

URL_CONST = 'https://www.amazon.com.br/s?i=stripbooks&bbn=6740748011&rh=p_n_specials_match%3A21225669011&s=price-desc-rank&dc&page='
LAST_PAGE = 10 # Inclusive the LAST_PAGE
FILENAME = 'amazon-books-sale.csv'


# Return all the pages links and save it in a list
# (could be a txt, it would be better tough?)
def get_links():
    page = 1
    total_pages = 1 + LAST_PAGE
    links_list = []
    while page < total_pages:
        url = URL_CONST + str(page)
        links_list.append(url)
        page += 1
    return links_list


# Acess each link and return all the info as a string
def get_info(url):
    # Sometimes the get method may face some bugs, doing a infinite loop force it to work properly
    while True:
        html_text = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}).text
        soup = BeautifulSoup(html_text, 'html.parser')
        items = soup.find_all('div', {'data-component-type':'s-search-result'})
        if items != []:
            break
    info_ls = []
    # Iterate over each item (product)
    for item in items:

        name = item.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
        
        # This Try and Except thing is necessary because there is differences bewtween the way
        # each item info is organized
        try: subtitle = item.find('div', {'class': 'a-row a-size-base a-color-secondary'}).text
        
        except: subtitle = None
        
        try: stars = item.find('span', {'class': 'a-icon-alt'}).text.replace(' de 5 estrelas', '/5')   
        except: stars = None
        
        try: reviews = int(item.find_all('span', {'class': 'a-size-base'})[-1].text)
        except: reviews = None
            
        try: price = float(item.find('span', {'class': 'a-offscreen'}).text.replace('R$', '').replace(',', '.').strip())
        except: price = None
        
        try:
            shipping_div = item.find('div', {'class':'a-row a-size-base a-color-secondary s-align-children-center'})
            shipping_span = shipping_div.find_all('span')[-1].text
            if 'GRÁTIS' in shipping_span:
                shipping = 0
            elif 'R$' in shipping_span:
                shipping = float(shipping_span.replace('R$', '').replace(' de frete', ''). replace(',', '.').strip())
            else:
                shipping = None
        except: shipping = None
        
        info = f'"{name}","{subtitle}",{stars},{reviews},{price},{shipping}'
        info_ls.append(info)
        
    return info_ls

    
# Store the info in a file (csv, txt...)
def store_info(filename, items):
    with open(filename, 'a', encoding='UTF-8') as csv:
        for item in items:
            csv.write(item + '\n')
    print('Web Scapping == Finished Sucessfuly')


# Puts everything together (juntos e shallow now)
def main():
    urls = get_links()
    for url in urls:
        print('\n', url)
        items = get_info(url)
        store_info(FILENAME, items)


if __name__ == '__main__':
    main()