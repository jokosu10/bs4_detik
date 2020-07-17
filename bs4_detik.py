import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(url.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})

titles_popular_area = populer_area.find_all(attrs={'class': 'media__title'})
images_popular_area = populer_area.find_all(attrs={'class': 'media__image'})

# for i in titles_popular_area:
#     print(i.text)

for i in images_popular_area:
    print(i.find('a').find('img'))
