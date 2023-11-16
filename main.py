from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import pprint


app = FastAPI()
app.title = 'Curso FastAPI'
app.version = '0.2'


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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
