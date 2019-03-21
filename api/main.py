import os

import delighted
from config import api_key

delighted.api_key = os.getenv('API_KEY')

responses = delighted.SurveyResponse.all()
