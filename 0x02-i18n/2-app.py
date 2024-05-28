#!/usr/bin/env python3
"""2. Get locale from request"""
from flask_babel import flask_babel
from flask import Flask, render_template, request


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)