import requests
import time
from plyer import notification
import creads

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apikey="+creads.api_key
    news = requests.get(main_url).json()
    article = news["articles"]
    news_article = []
    for arti in article:
        news_article.append(arti['title'])

    mes=""
    for i in range(1):
        mes = mes+f"{i+1}) {news_article[i]}"+ "\n"
    print(mes)
 
    if __name__ == "__main__":
        while True:
            notification.notify(
                title="Daily News",
                app_icon="C:\\Users\\dwive\\OneDrive\\Desktop\\DSA PY\\Python\\NEW PROJECTS\\Pelfusion-Folded-Flat-News.ico",
                message= mes,
                timeout=2
            )
            time.sleep(60*60)
news()
