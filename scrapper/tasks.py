from celery import shared_task
from celery.contrib import rdb
import requests
from bs4 import BeautifulSoup
from .models import Proxy

@shared_task
def scrape_proxies():
    url = 'https://geonode.com/free-proxy-list'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    proxies = []

    table = soup.find('table', class_='free-proxies-table')
    for row in soup.find('table', class_='free-proxies-table'):
        data = [td.get_text(strip=True) for td in row.find_all('td')]
        
        print(data)
        if len(data) == 8:
            ip, port, protocol, country, uptime = data[:5]
            proxies.append(Proxy(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime))
    
    Proxy.objects.bulk_create(proxies)
    print(proxies)




