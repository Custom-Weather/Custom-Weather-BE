import bs4
import requests
import json
import random

# Download IMDB's Top 250 data

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
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    place = movie[:len(str(index))-(len(movie))]
    # data = {"movie_title": movie_title, "place": place}
    imdb.append(movie_title)

# THIS WILL PRINT THE ENTIRE 250 LIST
# for item in imdb:
# print(item['place'], '-', item['movie_title'])
# print(item['movie_title'])

random_movies = random.sample(imdb, 10)

movies = {'movie1': f'{random_movies[0]}',
         'movie2': f'{random_movies[1]}',
         'movie3': f'{random_movies[2]}',
         'movie4': f'{random_movies[3]}',
         'movie5': f'{random_movies[4]}',
         'movie6': f'{random_movies[5]}',
         'movie7': f'{random_movies[6]}',
         'movie8': f'{random_movies[7]}',
         'movie9': f'{random_movies[8]}',
         'movie10': f'{random_movies[9]}',
         }

json_object_top_movies = json.dumps(movies)
print(json_object_top_movies)