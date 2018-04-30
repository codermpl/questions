import math

from flask import Flask, jsonify, render_template, request
from waitress import serve
from werkzeug.contrib.cache import SimpleCache

from app.file_import import import_csv
from app.customJSONEncoder import CustomJSONEncoder
import app.question_service as question_service

cache = SimpleCache(default_timeout=0)
DEFAULT_PAGE_SIZE = 20

def setup_server():
    new_app = Flask(__name__, static_url_path='', static_folder='static')
    questions = import_csv('code_challenge_question_dump.csv')
    cache.set('questions', questions)
    cache.set('default_total_pages', math.ceil(len(questions) / DEFAULT_PAGE_SIZE))
    new_app.json_encoder = CustomJSONEncoder
    return new_app

app = setup_server()


@app.route("/rest/question")
def get_all():
    page = int(request.args.get('page', None))
    size = int(request.args.get('size', 20))
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
    return render_template('index.html')

if __name__ == "__main__":
    new_app = setup_server()
    serve(new_app, host='0.0.0.0', port=33507)

