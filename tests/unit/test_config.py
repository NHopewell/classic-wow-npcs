import os


def test_development_config(test_app):
    # given 
    test_app.config.from_object('classic_wow_npcs.config.DevelopmentConfig')

    # then
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')


def test_testing_config(test_app):
    # given
    test_app.config.from_object('classic_wow_npcs.config.TestingConfig')

    # then
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert test_app.config['TESTING']
    assert not test_app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')


def test_production_config(test_app):
    # given
    test_app.config.from_object('classic_wow_npcs.config.ProductionConfig')

    # then
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')