from flask import Blueprint, jsonify, request
import config
import mysql.connector

blueprint_http = Blueprint('blueprint_http', __name__)

cnx = mysql.connector.connect(user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, database=config.DB_NAME)
query_reviews = ('SELECT r.id, r.name, r.comment, c.review_id as linked_id FROM reviews r LEFT JOIN curated_reviews c on c.review_id=r.id')
query_curated_reviews = ('SELECT name, comment, gender FROM curated_reviews')
insert_curated_reviews = ('INSERT INTO curated_reviews (review_id, comment, name, gender) VALUES (%s, %s, %s, %s)')

@blueprint_http.route('/api/external-reviews')
def external_reviews():
    response = {
        'reviews' : [],
        'total' : 0
    }
    cursor = cnx.cursor()
    cursor.execute(query_reviews)
    for (review_id, name, comment, linked_id) in cursor:
        review = {
            'id' : review_id,
            'name' : name,
            'quote' : comment,
            'is_curated': linked_id is not None
        }
        response['reviews'].append(review)
        response['total'] = response['total'] + 1
    cursor.close()
    return jsonify(response)

@blueprint_http.route('/api/curated-reviews/<review_id>', methods=['POST'])
def add_curated_reviews(review_id):
    cursor = cnx.cursor()
    body = request.get_json()
    cursor.execute(insert_curated_reviews, (review_id, body['quote'], body['name'], body['gender']))
    cnx.commit()
    cursor.close()
    response = {
        'status': 'Successfully added curated review'
    }
    return jsonify(response)

@blueprint_http.route('/api/curated-reviews')
def get_curated_reviews():
    cursor = cnx.cursor()
    response = {
        'reviews' : [],
        'total' : 0
    }
    cursor.execute(query_curated_reviews)
    for (name, comment, gender) in cursor:
        review = {
            'name' : name,
            'quote' : comment,
            'gender' : gender
        }
        response['reviews'].append(review)
        response['total'] = response['total'] + 1
    cursor.close()
    return jsonify(response)
