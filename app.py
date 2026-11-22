from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root(Name: str):
    return {"message": f"Hello, {Name}!"}

@app.get("/ping")
def ping():
    return {"message": f"Понг"}

@app.post("/post/ping")
def post_ping():
     return {"message": f"Понг с поста"}