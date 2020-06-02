import bs4
import requests
import json

def getBooks():
  res = requests.get('https://www.goodreads.com/shelf/show/trending')
  res.raise_for_status

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.find_all("a", class_="bookTitle")[0:10]
  elems = [i.text for i in elems]
  trending_books = {'book1': f'{elems[0]}',
          'book2': f'{elems[1]}',
          'book3': f'{elems[2]}',
          'book4': f'{elems[3]}',
          'book5': f'{elems[4]}',
          'book6': f'{elems[5]}',
          'book7': f'{elems[6]}',
          'book8': f'{elems[7]}',
          'book9': f'{elems[8]}',
          'book10': f'{elems[9]}' 
          }
  # json_object_trending_books = json.dumps(trending_books)
  return trending_books