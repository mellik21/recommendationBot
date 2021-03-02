from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import constantKeeper as keeper

driver = webdriver.Chrome(keeper.CHROME_DRIVER_PATH)

names = []
hrefs = []
genres = []
ratings = []

# put it in cycle
driver.get("https://smotret-anime.online/anime?page=1")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for anime_div in soup.findAll('div', attrs={'class': 'col s12 m4 l3'}):
    name = anime_div.find('h5', attrs={'class': 'line-1'})
    a = name.find('a', href=True)
    href = a['href']

    driver.get("https://smotret-anime.online" + href)
    c = driver.page_source
    s = BeautifulSoup(c, "html.parser")
    local_genres = []
    for genre_a in s.findAll('a', attrs={'class': 'm-genres-list__item'}):
        local_genres.append(genre_a.text)

    genres.append(local_genres)
    hrefs.append(href)
    names.append(name.text)

df = pd.DataFrame({'Name': names, 'Href': hrefs, 'Genres': genres})
df.to_csv('z_anime.csv', index=False, encoding='utf-8')
