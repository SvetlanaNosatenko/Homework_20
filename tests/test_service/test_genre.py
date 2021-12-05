from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genres_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Horror')
    genre_2 = Genre(id=2, name='Comedy')
    genre_3 = Genre(id=3, name='Thriller')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genres_dao):
        self.genre_service = GenreService(dao=genres_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "Horror"
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {"id": 3,
                   "name": "Horror"
                   }
        self.genre_service.update(genre_d)
