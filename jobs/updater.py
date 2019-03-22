import os

import delighted
from flask import Flask, request, jsonify
import mysql.connector
from aylienapiclient import textapi

delighted.api_key = os.getenv('API_KEY')

text_client = textapi.Client(os.getenv('AYLIEN_ID'), os.getenv('AYLIEN_KEY'))

add_review = ("INSERT INTO reviews (name, email, comment, order_id, seatgeek_message, created, polarity) VALUES (%s, %s, %s, %s, %s, %s, %s)")

def pull_reviews(cursor):
    responses = delighted.SurveyResponse.all(expand=['person'], order='desc',per_page=100)
    for response in responses:
        review = {
            'name': response.person['name'],
            'email': response.person['email'],
            'comment': response['comment'],
            'created': response['created_at'],
            'order_id': response['person_properties'].get('order_id', -1),
            'seatgeek_message': response['person_properties'].get('delighted_intro_message', ''),
        }
        if review['comment'] is None or review['comment'] == '':
            continue
        if review['name'] is None:
            review['name'] = ''
        if review['email'] is None:
            review['email'] = ''
        sentiment = text_client.Sentiment({'text' : review['comment'], 'mode' : 'document'})
        polarity = sentiment['polarity']
        review['polarity'] = polarity
        print(review['polarity'])
        cursor.execute(add_review, (review['name'], review['email'], review['comment'], review['order_id'], review['seatgeek_message'], review['created'], review['polarity']))

if __name__ == '__main__':
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    cursor = cnx.cursor()
    pull_reviews(cursor)
    cnx.commit()
    cursor.close()
    cnx.close()
