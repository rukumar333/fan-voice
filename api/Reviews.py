import os
import delighted

delighted.api_key = os.getenv('API_KEY')

class Reviews:
    def __init__(self):
        self.people = list()
        self.reviews = list()
        self.reviews_response = list()
        responses = delighted.SurveyResponse.all(order='desc')
        with open('response.json','w+') as f:
            f.write(str(responses))
        print(responses)

    def update_people(self):
        people = delighted.People.all()
        print(people)
