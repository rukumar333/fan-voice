import os

import delighted

from flask import Flask, request, jsonify

delighted.api_key = os.getenv('API_KEY')

def pull_reviews():
    responses = delighted.SurveyResponse.all(expand=['person'], order='desc',per_page=100)
    reviews = list()
    for response in responses:
        review = {
            'name': response.person['name'],
            'email': response.person['email'],
            'comment': response['comment'],
            'created': response['created_at'],
            'order_id': response['person_properties'].get('order_id', -1),
            'seatgeek_message': response['person_properties'].get('delighted_intro_message', '')
        }
        reviews.append(review)
        print(len(reviews))
        print(reviews)
    return reviews

@app.route('/api/reviews/reviews')
def get_reviews():
    
