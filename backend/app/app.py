from fastapi import FastAPI
from schemas import UserInfo

app = FastAPI()

@app.get('/')
def root():
	return {"Hello": "World"}
	

@app.post("/results")
def calculate_salary(criteria: SearchCriteria):
	return criteria