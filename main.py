from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import pprint


app = FastAPI()
app.title = 'Curso FastAPI'
app.version = '0.2'
'''
movies = [
    {
    "id": 1,
    "title": "Avatar",
    "overview": ":V",
    "year": "2009",
    "rating": 7.8,
    "category": "Accion"
    },
    {
    "id": 2,
    "title": "Vengadores",
    "overview": ":V",
    "year": "2010",
    "rating": 6,
    "category": "Aventura"
    }
]
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []

'''

@app.get('/movies/{show_id}', tags=['movies'])
def get_movies_by_id(show_id:str):
    print(show_id)

    with open('convertcsv.json','r') as f:
        array = json.load(f)

    show_id = 's' + show_id
    for item in array:
        if show_id in item.get("show_id"):
            item_dict = item
            return item
            #pprint.pprint(item)
            #break
    return []