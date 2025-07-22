from fastapi import FastAPI
from schemas import UserInfo
from ../dev_salary_prediction_model import salary_calculation_model

app = FastAPI()

@app.get('/')
def root():
	return {"Hello": "World"}

@app.post("/results")
def calculate_salary(criteria: SearchCriteria):
	predicted_salary = salary_calculation_model(criteria)
	return predicted_salary