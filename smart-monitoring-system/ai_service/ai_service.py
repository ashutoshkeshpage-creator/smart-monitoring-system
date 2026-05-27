from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    temperature: float
    humidity: int

@app.post("/analyze")
def analyze(data: SensorData):

    temp = data.temperature

    # Temperature conditions in Celsius
    if temp > 40:
        result = "Possible overheating"
        status = "HOT ALERT"

    elif temp < 10:
        result = "Possible freezing conditions"
        status = "COLD ALERT"

    else:
        result = "Normal temperature"
        status = "SAFE"

    return {
        "temperature_celsius": temp,
        "status": status,
        "result": result
    }