from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import config as keeper
import components

'''Парсинг сайта и формирование anime.base.csv'''

driver = webdriver.Chrome(keeper.CHROME_DRIVER_PATH)
rus_names, eng_names, hrefs, genres, ratings, descriptions, alt_descriptions, minor_names, img_paths, pages, additional = \
    ([] for _ in range(11))


def appendTextOrAttr(value, list, attr=None):
    if value is not None:
        if attr is not None:
            list.append(value[attr])
        else:
            list.append(value.text)
    else:
        list.append("")


def initDf():
    df = pd.DataFrame({'Page': pages,
                       'Rus_name': rus_names,
                       'Eng_name': eng_names,
                       'Href': hrefs,
                       'Genres': genres,
                       'Rating': ratings,
                       'Description': descriptions,
                       'Alt_description': alt_descriptions,
                       'Img': img_paths,
                       'Minor_names': minor_names,
                       'Additional': additional})
    df.to_csv('anime.csv', index=False, encoding='utf-8')


def appendDf():
    previous_data = pd.read_csv('files/anime.csv')
    df = pd.DataFrame({'Page': pages,
                       'Rus_name': rus_names,
                       'Eng_name': eng_names,
                       'Href': hrefs,
                       'Genres': genres,
                       'Rating': ratings,
                       'Description': descriptions,
                       'Alt_description': alt_descriptions,
                       'Img': img_paths,
                       'Minor_names': minor_names,
                       'Additional': additional})
    previous_data = previous_data.append(df, ignore_index=True)
    previous_data.to_csv('anime.csv', index=False, encoding='utf-8')


def clear():
    #  del genres[-1]    del hrefs[-1]
    del rus_names[-1]
    del eng_names[-1]


def parse(left, right):
    for i in range(left, right):
        driver.get("https://smotret-anime.online/anime?page=" + str(i))
        parser = BeautifulSoup(driver.page_source, "html.parser")

        '''Перебор всех фильмов на текущей странице'''
        for anime_div in parser.findAll('div', attrs={'class': 'col s12 m4 l3'}):
            eng_name = anime_div.find('h4', attrs={'class': 'line-2'})
            appendTextOrAttr(eng_name, eng_names)
            rus_name = anime_div.find('h5', attrs={'class': 'line-1'})
            appendTextOrAttr(rus_name, rus_names)

            a = rus_name.find('a', href=True)
            href = a['href']

            '''Переход на страницу фильма для выбора более полной информации'''
            driver.get("https://smotret-anime.online" + href)
            p = BeautifulSoup(driver.page_source, "html.parser")
            rating = p.find('span', attrs={'itemprop': 'ratingValue'})

            if rating is None:
                clear()
                continue
            appendTextOrAttr(rating, ratings)
            hrefs.append(href)
            pages.append(i)

            local_genres = []
            for genre_a in p.findAll('a', attrs={'class': 'm-genres-list__item'}):
                appendTextOrAttr(genre_a, local_genres)
            genres.append(local_genres)

            descs = p.findAll('div', attrs={'class': 'm-description-item'})
            desc1 = descs[0].find('div', attrs={'class': 'card-content'}) if len(descs) > 0 else ""
            desc2 = descs[1].find('div', attrs={'class': 'card-content'}) if len(descs) > 1 else ""
            descriptions.append(desc1.text if len(descs) > 0 else "")
            alt_descriptions.append(desc2.text if len(descs) > 1 else "")

            local_minor_names = p.find('div', attrs={'class': 'm-minor-titles-list'})
            appendTextOrAttr(local_minor_names, minor_names)

            img = p.find('img', attrs={'itemprop': 'contentUrl'})
            appendTextOrAttr(img, img_paths, 'src')

            addition = ""
            for card in p.findAll('div', attrs={'class': 'card-content'}):
                cards_p = card.find('p')
                if cards_p is not None:
                    addition = cards_p.text
                    break

            additional.append(addition)


# parse(1, 2)
# initDf()
parse(71, 81)
appendDf()
