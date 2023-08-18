import requests

label_mapping = {0: "Audi", 1: "Hyundai Creta", 2: "Mahindra Scorpio",
                3: "Rolls Royce", 4: "Swift", 5: "Tata Safari",
                6:"Toyota Innova"}



def predict_car(image, m):
    url = "http://172.17.0.1:8080/api/genhog"
    params = {"img_base64": image}
    response = requests.get(url, json=params)
    res = response.json()
    hogList = list(res.values())
    car_predict = m.predict(hogList)
    car_brand = label_mapping.get(car_predict[0])
    return car_brand
    