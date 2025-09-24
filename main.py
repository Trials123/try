from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def news():
    return {"message": "Hello World"}