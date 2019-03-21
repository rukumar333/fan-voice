import os

import delighted

delighted.api_key = os.getenv('API_KEY')

responses = delighted.SurveyResponse.all(order='desc')
print(responses)
