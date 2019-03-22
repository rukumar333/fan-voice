from flask import Blueprint, jsonify

blueprint_http = Blueprint('blueprint_http', __name__)

@blueprint_http.route('/api/external-reviews')
def external_reviews():
    return jsonify({
        'reviews': [
            {'name': 'George Daole-Wellman', 'text': 'SeatGeek is great'},
            {'name': 'Rushil Kumar', 'text': 'It\s the best'},
            {'name': 'Locke Anderson', 'text': 'Awesome'}
        ],
        'total': 3
    })
