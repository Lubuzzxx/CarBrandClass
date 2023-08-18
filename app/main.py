from fastapi import FastAPI, Request
from app.code import callAPI
import pickle
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model = pickle.load(open(r'../model/car_model.pkl', 'rb'))
model = pickle.load(open(os.getcwd() + r'/model/car_model.pkl', 'rb'))


@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/carbrand")
async def read_str(data: Request):
    json = await data.json()
    image_str = json['img_base64']
    car_brand = callAPI(image_str, model)

    return {"car brand": car_brand}