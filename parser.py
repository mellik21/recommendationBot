from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import constantKeeper as keeper
import common

'''Парсинг сайта и формирование anime.csv'''

driver = webdriver.Chrome(keeper.CHROME_DRIVER_PATH)
rus_names, eng_names, hrefs, genres, ratings, descriptions, alt_descriptions, studios, minor_names, img_paths, pages, additional = \
    ([] for _ in range(12))


def initDf():
    df = pd.DataFrame({'Page': pages,
                       'Rus_name': rus_names,
                       'Eng_name': eng_names,
                       'Href': hrefs,
                       'Genres': genres,
                       'Rating': ratings,
                       'Description': descriptions,
                       'Imgs': img_paths,
                       'Studios': studios,
                       'Minor_names': minor_names,
                       'Additional': additional})
    df.to_csv('anime.csv', index=False, encoding='utf-8')


def appendDf():
    previous_data = pd.read_csv('anime.csv')
    df = pd.DataFrame({'Page': pages,
                       'Rus_name': rus_names,
                       'Eng_name': eng_names,
                       'Href': hrefs,
                       'Genres': genres,
                       'Rating': ratings,
                       'Description': descriptions,
                       'Imgs': img_paths,
                       'Studios': studios,
                       'Minor_names': minor_names,
                       'Additional': additional})
    previous_data = previous_data.append(df, ignore_index=True)
    previous_data.to_csv('anime.csv', index=False, encoding='utf-8')

for i in range(1, 11):
    driver.get("https://smotret-anime.online/anime?page=" + str(i))
    parser = BeautifulSoup(driver.page_source, "html.parser")

    '''Перебор всех фильмов на текущей странице'''
    for anime_div in parser.findAll('div', attrs={'class': 'col s12 m4 l3'}):
        eng_name = anime_div.find('h4', attrs={'class': 'line-2'})
        common.appendTextOrAttr(eng_name, eng_names)
        rus_name = anime_div.find('h5', attrs={'class': 'line-1'})
        common.appendTextOrAttr(rus_name, rus_names)

        a = rus_name.find('a', href=True)
        href = a['href']
        hrefs.append(href)

        '''Переход на страницу фильма для выбора более полной информации'''
        driver.get("https://smotret-anime.online" + href)
        pages.append(i)
        p = BeautifulSoup(driver.page_source, "html.parser")
        local_genres, local_descriptions, local_studios = ([] for _ in range(3))
        for genre_a in p.findAll('a', attrs={'class': 'm-genres-list__item'}):
            local_genres.append(genre_a.text)
        genres.append(local_genres)

        for desc_div in p.findAll('div', attrs={'class': 'm-description-item'}):
            desc = desc_div.find('div', attrs={'class': 'card-content'})
            local_descriptions.append(desc.text)
        descriptions.append(local_descriptions)

        for studio_a in p.findAll('a', attrs={'class': 'm-studios-list_item'}):
            local_studios.append(studio_a['href'])
        studios.append(local_studios)

        local_minor_names = p.find('div', attrs={'class': 'm-minor-titles-list'})
        common.appendTextOrAttr(local_minor_names, minor_names)

        rating = p.find('span', attrs={'itemprop': 'ratingValue'})
        common.appendTextOrAttr(rating, ratings)

        img = p.find('img', attrs={'itemprop': 'contentUrl'})
        common.appendTextOrAttr(img, img_paths, 'src')
        
        addition = p.find('div', attrs={'class': 'card-content'}).find('p')
        common.appendTextOrAttr(addition, additional)

appendDf()
