from fastapi import FastAPI

app = FastAPI()

@app.get('/get')
def func():
    print("Hello")
    return {"Message":"Hello world"}


