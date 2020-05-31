import bs4
import requests
import json

def getBooks(url):
    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.find_all("a", class_="bookTitle")[0:10]
    elems = [i.text for i in elems]
    return elems

books = getBooks('https://www.goodreads.com/shelf/show/trending')

trending_books = {'book1': f'{books[0]}',
         'book2': f'{books[1]}',
         'book3': f'{books[2]}',
         'book4': f'{books[3]}',
         'book5': f'{books[4]}',
         'book6': f'{books[5]}',
         'book7': f'{books[6]}',
         'book8': f'{books[7]}',
         'book9': f'{books[8]}',
         'book10': f'{books[9]}',
         }

json_object_trending_books = json.dumps(trending_books)
print(json_object_trending_books)