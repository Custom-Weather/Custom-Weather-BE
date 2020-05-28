import bs4
import requests
import json

def getMovies(url):
  res = requests.get(url)
  res.raise_for_status

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select('td.titleColumn')[0:10]
  # movie_string = elems[index].get_text()
  # movie = (' '.join(movie_string.split()).replace('.', ''))
  elems = [i.get_text() for i in elems]
  return elems

movies = getMovies('https://www.imdb.com/chart/moviemeter/')

print(len(movies))
print(movies)

# IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "place": place,
            "rating": ratings[index],
            "link": links[index]}
    imdb.append(data)

# for item in imdb:
#     print(item['place'], '-', item['movie_title'])
