from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import constantKeeper as keeper

driver = webdriver.Chrome(keeper.CHROME_DRIVER_PATH)
rus_names, eng_names, hrefs, genres, ratings, descriptions, alt_descriptions, studios, minor_names = ([] for _ in
                                                                                                      range(9))

driver.get("https://smotret-anime.online/anime?page=1")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for anime_div in soup.findAll('div', attrs={'class': 'col s12 m4 l3'}):
    eng_name = anime_div.find('h4', attrs={'class': 'line-2'})
    rus_name = anime_div.find('h5', attrs={'class': 'line-1'})
    a = rus_name.find('a', href=True)
    href = a['href']

    driver.get("https://smotret-anime.online" + href)
    c = driver.page_source
    s = BeautifulSoup(c, "html.parser")
    local_genres = []
    for genre_a in s.findAll('a', attrs={'class': 'm-genres-list__item'}):
        local_genres.append(genre_a.text)

    local_descriptions = []
    for desc_div in s.findAll('div', attrs={'class': 'm-description-item'}):
        desc = desc_div.find('div', attrs={'class': 'card-content'})
        local_descriptions.append(desc.text)

    local_studios = []
    for studio_a in s.findAll('a', attrs={'class': 'm-studios-list_item'}):
        local_studios.append(studio_a['href'])

    local_minor_names = s.find('div', attrs={'class': 'm-minor-titles-list'})

    if local_minor_names is not None:
        minor_names.append(local_minor_names.text)
    else:
        minor_names.append("")

    studios.append(local_studios)
    descriptions.append(local_descriptions)
    genres.append(local_genres)
    hrefs.append(href)
    rus_names.append(rus_name.text)
    eng_names.append(eng_name.text)
print(len(rus_names), len(eng_names), len(hrefs), len(genres), len(descriptions), len(studios), len(minor_names))
df = pd.DataFrame({'Rus_name': rus_names,
                   'Eng_name': eng_names,
                   'Href': hrefs,
                   'Genres': genres,
                   #     'Rating': ratings,
                   'Description': descriptions,
                   #   'Alt_desc': alt_descriptions,
                   'Studios': studios,
                   'Minor_names': minor_names})
df.to_csv('anime.csv', index=False, encoding='utf-8')
