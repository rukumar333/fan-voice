from flask import Blueprint, jsonify, request
import config
import mysql.connector

blueprint_http = Blueprint('blueprint_http', __name__)

cnx = mysql.connector.connect(user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, database=config.DB_NAME)
query_reviews = ('SELECT name, comment FROM reviews')
query_curated_reviews = ('SELECT name, comment, gender FROM curated_reviews')

@blueprint_http.route('/api/external-reviews')
def external_reviews():
    response = {
        'reviews' : [],
        'total' : 0
    }
    cursor = cnx.cursor()
    cursor.execute(query_reviews)
    for (name, comment) in cursor:
        review = {
            'name' : name,
            'text' : comment
        }
        response['reviews'].append(review)
        response['total'] = response['total'] + 1
    cursor.close()
    return jsonify(response)

@blueprint_http.route('/api/curated-reviews', methods=['GET', 'POST'])
def curated_reviews():
    cursor = cnx.cursor()
    if request.method == 'POST':
        print('Adding curated review')
    else:
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
