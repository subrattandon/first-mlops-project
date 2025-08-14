from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# ✅ CORS fix (frontend se API call allow karne ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tu chahe to ["http://localhost:5500"] bhi rakh sakta hai
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model load
model = joblib.load("diabetes_model.pkl")

# Input data format
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live"}

@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.BMI, data.Age]])
    prediction = model.predict(input_data)[0]
    return {"diabetic": bool(prediction)}
