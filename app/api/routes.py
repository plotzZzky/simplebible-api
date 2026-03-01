from flask import request, Response, Flask, render_template
from app.api.db import find_in_bible
from app.api.utils import format_query


app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def get_html_bible():
    book = request.args.get('book', default=None)
    capt = request.args.get('capt', default=None)
    vers = request.args.get('vers', default=None)

    query = find_in_bible(book, capt, vers)
    result = format_query(query)

    return Response(result)


@app.route('/api')
def get_json_bible():
    book = request.args.get('book', default=None)
    capt = request.args.get('capt', default=None)
    vers = request.args.get('vers', default=None)

    query = find_in_bible(book, capt, vers)
    result = format_query(query, 'json')

    return Response(result, mimetype='application/json')


@app.route('/txt')
def get_txt_bible():
    book = request.args.get('book', default=None)
    capt = request.args.get('capt', default=None)
    vers = request.args.get('vers', default=None)

    query = find_in_bible(book, capt, vers)
    result = format_query(query, 'txt')

    return Response(result, mimetype='text/plain')
