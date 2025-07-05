from fastapi import FastAPI, HTTPException
import pickle
from schemas import UserInfo

app = FastAPI()

#def predict_salary(data: UserInfo):
@app.get('/')
def read_root():
	return {"Hello": "World"}
	#try:
		# Extract features from the input data
	#	data_dict = data.model_dump()
	#	user_features = [data_dict['education_level'],data_dict['years_coding_professionally'],
	#					 data_dict['job_title'],data_dict['company_size'],
	#					 data_dict['location']]

		# Make prediction of future salary using the pre-loaded model
		##prediction = classifier.predict([user_features])[0]

		##return {'predicted salary': prediction}
	#	return user_features['education_level']

	#except Exception as e:
	#	raise HTTPException(status_code=500, detail=f"Error occured: {e}")