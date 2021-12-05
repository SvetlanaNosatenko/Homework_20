from unittest.mock import MagicMock
import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Movie_1', description='description_1', trailer='trailer_1', year=2018,
                    rating=1, genre_id=1, director_id=2)
    movie_2 = Movie(id=2, title='Movie_2', description='description_2', trailer='trailer_2', year=2019,
                    rating=3, genre_id=2, director_id=7)
    movie_3 = Movie(id=3, title='Movie_3', description='description_3', trailer='trailer_3', year=2020,
                    rating=5, genre_id=5, director_id=9)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=1))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'title_1',
            'description': 'description_1',
            'trailer': 'trailer_1',
            'year': 2019,
            'rating': 2,
            'genre_id': 2,
            'director_id': 2,
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {'id': 3,
                   'title': 'title_3',
                   'description': 'description_1',
                   'trailer': 'trailer_1',
                   'year': 2019,
                   'rating': 2,
                   'genre_id': 2,
                   'director_id': 2,
                   }
        self.movie_service.update(movie_d)
