from django.db import models
from celery import shared_task
from urllib.request import urlopen
from bs4 import BeautifulSoup
from demoapp.models import Job




@shared_task(name="repeat_scrap_make")
def repeat_scrap_make():
    
    # собираем html
    html = urlopen('https://krasnodar.hh.ru/search/vacancy?text=django&from=suggest_post&fromSearchLine=true&area=53')

    # преобразуем в soup-объект
    soup = BeautifulSoup(html, 'html.parser')

    # собираем все посты
    postings = soup.find_all("div", class_="serp-item")

    for p in postings:
        url = p.find('a', class_='bloko-link')['href']
        title = p.find('a', class_='bloko-link').text
        company = p.find('div', class_='bloko-text').text        # check if url in db
        
        try:        # сохраняем в базе данных
            Job.objects.create(
                url=url,
                title=title,
                company=company,            )
            print('%s added' % (title,))
            print( 'job complete' )


        except:
            print('%s allready exist' % (title,))

    