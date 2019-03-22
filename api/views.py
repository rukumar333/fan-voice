from flask import Blueprint, jsonify, request
import config
import mysql.connector

blueprint_http = Blueprint('blueprint_http', __name__)

cnx = mysql.connector.connect(user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, database=config.DB_NAME)
query_reviews = ('SELECT r.id, r.name, r.comment, c.review_id as linked_id FROM reviews r LEFT JOIN curated_reviews c on c.review_id=r.id WHERE r.comment LIKE %s')
query_reviews_limit = ('SELECT r.id, r.name, r.comment, c.review_id as linked_id FROM reviews r LEFT JOIN curated_reviews c on c.review_id=r.id WHERE r.comment LIKE %s AND CHAR_LENGTH(r.comment) < %s')
query_curated_reviews = ('SELECT name, comment, gender FROM curated_reviews')
query_curated_reviews_limit = ('SELECT name, comment, gender FROM curated_reviews WHERE CHAR_LENGTH(comment) < %s')
insert_curated_reviews = ('INSERT INTO curated_reviews (review_id, comment, name, gender) VALUES (%s, %s, %s, %s)')

@blueprint_http.route('/api/external-reviews')
def external_reviews():
    response = {
        'reviews' : [],
        'total' : 0
    }
    keyword = request.args.get('keyword', '')
    char_limit = request.args.get('char_limit', None)
    cursor = cnx.cursor()
    if char_limit is None:
        cursor.execute(query_reviews, ('%' + keyword + '%',))
    else:
        cursor.execute(query_reviews_limit, ('%' + keyword + '%', int(char_limit)))
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
    char_limit = request.args.get('char_limit', None)
    if char_limit is None:
        cursor.execute(query_curated_reviews)
    else:
        cursor.execute(query_curated_reviews_limit, (int(char_limit),))
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
