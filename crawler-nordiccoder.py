import sys
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    link = sys.argv[1]
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')

    title = soup.find('title')
    article = soup.find('article')
    author = article.find_all('p')[-1].find('strong')
    article_date = soup.find(class_='date')

    print('URL: ' + link)
    print('Title: ' + title.text)
    print('Author: ' + author.text)
    print('Date: ' + article_date.text)
