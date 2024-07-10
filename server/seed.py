#!/usr/bin/env python3
from models import Movie

from config import db, app


if __name__ == '__main__':
    with app.app_context():
        def create_movie_data():
            movies = ['Pulp Fiction', 'Star Trek', 'Kill Bill Volume1', 'No Country for Old Men' ]
            movie_list = []
            print("Deleting existing movie data...")
            Movie.query.delete()
            for movie in movies:
                movie_list.append(Movie(title=movie))
                
            db.session.add_all(movie_list)
            db.session.commit()
            print("Adding movie data...")
        create_movie_data()