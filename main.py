from fastapi import FastAPI



app = FastAPI()

@app.post("/news")
def create_news(items: list):

    return {"items": items}

@app.get("/")
def news():
    return {"message": "Hello World"}