import requests
from bs4 import BeautifulSoup

url = ('https://www.detik.com/terpopuler')
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

s = requests.session()
s.headers.update(headers)

page = s.get(url)

if page.status_code == 200:
    print('Request succedd')
else:
    print(f"Request failled with status code {page.status_code}")

def populer_news():
    soup = BeautifulSoup(page.text, 'html.parser')
    populer = soup.find('div',{'class':'grid-row list-content'})
    # print(populer)
    titles = populer.find_all(attrs={'class':'media__text'})
    images = populer.find_all(attrs={'class':'media__image'})
    for i in images:
        print(i.find('a').find('img')['title'])
    # print(titles)


if __name__ == '__main__':
    populer_news()