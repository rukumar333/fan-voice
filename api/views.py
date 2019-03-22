from flask import Blueprint, jsonify, request
import config
import mysql.connector

blueprint_http = Blueprint('blueprint_http', __name__)

cnx = mysql.connector.connect(user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, database=config.DB_NAME)

query_reviews = 'SELECT r.id, r.name, r.comment, c.review_id as linked_id FROM reviews r LEFT JOIN curated_reviews c on c.review_id=r.id WHERE r.comment LIKE %(keyword)s'

query_curated_reviews = 'SELECT name, comment, gender FROM curated_reviews'

insert_curated_reviews = ('INSERT INTO curated_reviews (review_id, comment, name, gender) VALUES (%s, %s, %s, %s)')

PER_PAGE = 20

@blueprint_http.route('/api/external-reviews')
def external_reviews():
    response = {
        'reviews' : [],
        'total' : 0
    }
    query = query_reviews
    query_params = { 'per_page' : PER_PAGE}
    keyword = request.args.get('keyword', '')
    query_params['keyword'] = '%' + keyword + '%'
    max_length = request.args.get('max_length', None)
    min_length = request.args.get('min_length', None)
    page = int(request.args.get('page', 1))
    offset = (page - 1) * PER_PAGE
    query_params['offset'] = offset
    cursor = cnx.cursor()
    if max_length is not None:
        query_params['max_length'] = max_length
        query = query + ' AND CHAR_LENGTH(r.comment) < %(max_length)s'
    if min_length is not None:
        query_params['min_length'] = min_length
        query = query + ' AND CHAR_LENGTH(r.comment) > %(min_length)s'
    query = query + ' LIMIT %(per_page)s OFFSET %(offset)s'
    cursor.execute(query, query_params)
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
    response['page'] = page
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
    query = query_curated_reviews
    query_params = {'per_page' : PER_PAGE}
    page = int(request.args.get('page', 1))
    offset = (page - 1) * PER_PAGE
    query_params['offset'] = offset
    query = query + ' LIMIT %(per_page)s OFFSET %(offset)s'
    cursor.execute(query, query_params)
    for (name, comment, gender) in cursor:
        review = {
            'name' : name,
            'quote' : comment,
            'gender' : gender
        }
        response['reviews'].append(review)
        response['total'] = response['total'] + 1
    cursor.close()
    response['page'] = page
    return jsonify(response)
