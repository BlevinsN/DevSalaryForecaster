from pydantic import BaseModel

class UserInfo(BaseModel):

	education_level: int
	years_coding_professionally: int
	job_title: int
	company_size: int
	location: str