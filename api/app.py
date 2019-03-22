from flask import Flask
import config
import views

flask_app = Flask(__name__)
flask_app.register_blueprint(views.blueprint_http)

views.blueprint_http.config = flask_app.config
flask_app.run(port=config.PORT)
