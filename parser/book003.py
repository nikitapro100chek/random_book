import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

def download(url):
    resp = requests.get(url, stream=True)
    r = open("\\Users\\a1\\Desktop\\Програмы\\Книги\\picture\\" + url.split("/")[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()    

def get_url():
    for count in range(2,350):
        url = f"https://akniga.org/section/roman/top/page{count}/?period=all" #- роман
        #"https://akniga.org/section/fantasy/top/page{count}/?period=all" #- фентази
        #
        #"https://akniga.org/section/classic/top/page{count}/?period=all" # rkfccbrf
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="content__main__articles--item")

        for f in data:
            card_url = f.find("a").get("href")
            yield card_url
    
def array():

    for card_url in get_url():

        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="content__main__articles content__article")
        name = data.find("div", class_="caption__article-main-mobile--container").text.replace("\n", "")#название
        longer = data.find("div", class_="full-width").text.replace("\n", "")#длительность
        about = data.find("div", class_="description__article-main").text.replace("\n", "")#описание
        comments = data.find("a", class_="link__action link__action--comments tap-link no-pjax").text.replace("\n", "")#коментарии
        #reader = data.find("a", class_="link__reader").text.replace("\n", "")#чтец icon icon-author link__reader
        url_img = data.find("img", class_="loaded").get("src")#картинка
        whotch = data.find("span", class_="link__action--label link__action--label--views pull-right").text.replace("\n", "")#просмотры
        like = data.find("div", class_="ls-vote-item ls-vote-item-up js-vote-item ls-counter").text.replace("\n", "")#лайки
        favourit = data.find("div", class_="ls-counter ls-favourite ls-favourite--has-counter js-favourite-topic ls-topic-favourite").text.replace("\n", "")#избранное
        #download(url_img)

        yield card_url, url_img, longer, whotch, like, comments, about #reader,
