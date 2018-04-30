import math, logging
from sys import stdout

from flask import Flask, jsonify, render_template, request
from waitress import serve
from werkzeug.contrib.cache import SimpleCache

from app.file_import import import_csv
from app.customJSONEncoder import CustomJSONEncoder
import app.question_service as question_service

cache = SimpleCache(default_timeout=0)
DEFAULT_PAGE_SIZE = 20
log = logging.getLogger(__name__)

def setup_server():
    """ Setup the flask app """
    logging.basicConfig(stream=stdout, level="INFO")
    log.info("Starting Server")

    new_app = Flask(__name__, static_url_path='', static_folder='static')
    questions = import_csv('code_challenge_question_dump.csv')
    cache.set('questions', questions)
    cache.set('default_total_pages', math.ceil(len(questions) / DEFAULT_PAGE_SIZE))
    new_app.json_encoder = CustomJSONEncoder

    log.info("Finished initializing Flask app")
    return new_app

app = setup_server()


@app.route("/rest/question")
def get_questions():
    """ Return questions to the user """
    log.info("Serving questions. Parameters: %s", request.args)
    page, size = question_service.get_pagination_params(request.args)

    sorts = question_service.get_sorts(request.args)

    questions = cache.get('questions')

    if size == DEFAULT_PAGE_SIZE:
        total_pages = cache.get('default_total_pages')
    else:
        total_pages = math.ceil(len(questions) / size)

    questions = question_service.get_questions(questions, page, size, sorts)
    return jsonify(last_page=total_pages, data=questions)

@app.route('/')
def root():
    """ Serve the html page """
    return render_template('index.html')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)

