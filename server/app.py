#!/usr/bin/env python3
from flask import make_response, render_template
from config import app
from models import Movie
from dotenv import load_dotenv

load_dotenv()



@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")



@app.route('/movies', methods=['GET'])
def movies():
    movies = [movie.to_dict() for movie in Movie.query.all()]
    response = make_response(movies, 200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
