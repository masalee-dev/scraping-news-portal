import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')

def detik_populer():
    url = ('https://www.detik.com/terpopuler')
    headers = {
        'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

    s = requests.session()
    s.headers.update(headers)

    page = s.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    populer = soup.find('div', {'class': 'grid-row list-content'})
        # print(populer)
    titles = populer.find_all(attrs={'class': 'media__text'})
    images = populer.find_all(attrs={'class': 'media__image'})

    return render_template('detik-scraper.html', images=images)

@app.route('/idr-rates')

def idr_rates():
    source = requests.get('https://www.floatrates.com/daily/idr.json')
    c_data = source.json()
    return render_template('idr-rates.html',datas=c_data.values())

if __name__ == '__main__':
    app.run(debug=True)