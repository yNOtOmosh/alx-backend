#!/usr/bin/env python 3
"""Use user locale"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return user.get(user_id)
    except ValueError:
        return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    """check url parameters."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale


    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale



    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('6-index.html')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)