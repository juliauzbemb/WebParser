import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'программирование']
HEADERS = {'Accept': 'text/html,application/xhtml+xml,'
                     'application/xml;q=0.9,image/avif,'
                     'image/webp,image/apng,'
                     '*/*;q=0.8,application/signed-exchange;'
                     'v=b3;q=0.9 ',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru-RU,ru;q=0.9,en-US;'
                              'q=0.8,en;q=0.7',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie':
               '_ym_uid=1639934666860889724; '
               '_ym_d=1639934666; '
               '_ga=GA1.2.122808168.1639934666; '
               '_gid=GA1.2.1540720803.1639934666; '
               'habr_web_home=ARTICLES_LIST_ALL; '
               'hl=ru; fl=ru; _ym_isad=2; '
               '__gads=ID=3bca2fb12a84bfaa:T=1639934668:'
               'S=ALNI_MagABWot_b98koFdCB4lM3aLC2RAA; '
               'cto_bundle'
               '=0wD_Y19KQmE2VSUyQmdwbFBWOGlDVGdGNlhL'
               'NnpDNEVUdGNKOWtQSlpHVjRXTXZqQVdoYkVkM'
               'kJDSGFHemd2OHhFY1lLT0g1UVlweEZYOWlBTmR'
               'GaGdlaW4zOEhCQlI1RWVNcEJEUjJHRWdjVTRFN'
               'mx3bmxhcnFMODlSWCUyRkdETmpOUnloWHZGQU1'
               'CV2hNV2duOG03aUNHcEpPTFhXS2dWRGFkMVNyT'
               'Tlyb1pwZ3psVlZ1b0ZyJTJCcVlEcFN3VEx3eE'
               'NCbEpEZ3o ',
           'Host': 'habr.com',
           'If-None-Match': 'W/"3a406-HWoKTAp/3V+g6gWQdD8MLds+0Ns"',
           'sec-ch-ua': '" Not A;Brand";v="99", '
                        '"Chromium";v="96", "Google Chrome";v="96"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': "macOS",
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/96.0.4664.110 Safari/537.36 '
           }

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
print(len(articles))

for article in articles:
    hubs = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
    hubs = [hub.find('span').text for hub in hubs]
    # print(hubs)
    title = article.find('a', class_="tm-article-snippet__title-link").text
    # print(title)
    link = article.find('a', class_="tm-article-snippet__title-link").\
        get('href')
    # print(link)
    article_preview = article.find('div', class_='article-formatted-body').text
    # print(article_preview)
    date = article.find('span',
                        class_='tm-article-snippet__datetime-published')
    datetime = date.find('time')['title']
    # print(datetime)

    for word in KEYWORDS:
        if (word.lower() in title.lower()) \
                or (word.lower() in article_preview.lower()) \
                or (word.capitalize() in hubs):
            print(f'Дата: {datetime} - Заголовок: {title} '
                  f'- Ссылка: {"habr.com" + link}')
