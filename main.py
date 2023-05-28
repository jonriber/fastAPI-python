from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"name":"root","data":"First Python API"}

@app.get("/my_name")
async def my_name():
    return {"name":"my_name","data":"My name is Jonatas Ribeiro"}

@app.get("/random/{limit}")
async def get_random(limit:int):
    random_number = random.randint(0,limit)
    return {"name":"get_random","data":random_number}
