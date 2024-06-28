from django.db import models
from celery import shared_task
from bs4 import BeautifulSoup
from demoapp.models import Job
import requests




@shared_task(name="repeat_scrap_make")
def repeat_scrap_make():
    
    # собираем html
    html = requests.get('https://krasnodar.hh.ru/search/vacancy?L_save_area=true&text=django&excluded_text=&area=53&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter', headers={'User-Agent': 'Custom'}, verify = False)

    # преобразуем в soup-объект
    soup = BeautifulSoup(html.text, 'html.parser')

    # собираем все посты
    postings = soup.find_all("div", class_="vacancy-search-item__card")


    for p in postings:
        url = p.find('a', class_='bloko-link')['href']
        title = p.find('span', class_='vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link').text
        company = p.find('span', class_='company-info-text--vgvZouLtf8jwBmaD1xgp').text        # check if url in db
        
        try:        # сохраняем в базе данных
            Job.objects.create(
                url=url,
                title=title,
                company=company,            )
            print('%s added' % (title,))
            print( 'job complete' )


        except:
            print('%s allready exist' % (title,))

    