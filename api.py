from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Coord(BaseModel):
    lat:float
    lon:float
    zoom:Optional[int]


@app.get("/")
async def hello_world():
    return {"hello":"world"}


@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id": component_id}

@app.get("/component/")
async def read_component(number: int, text:str):
    return {"number": number, "text": text}

@app.post("/position/")
async def make_position(coord:Coord):
    return coord.__dict__