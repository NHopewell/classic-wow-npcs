import pytest

from classic_wow_npcs import app, db


@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('classic_wow_npcs.config.TestingConfig')
    with app.app_context():
        yield app 


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()