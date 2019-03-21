import delighted
from config import api_key

delighted.api_key = api_key

responses = delighted.SurveyResponse.all()
