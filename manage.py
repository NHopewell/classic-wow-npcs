from flask.cli import FlaskGroup

from classic_wow_npcs import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()