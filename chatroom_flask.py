"""Flask module to provide Web App allowing user to enter a URL
and view the word count for the text at that address.
"""

from datetime import datetime
import os
import urllib


from flask import Flask, render_template, redirect, url_for, session, jsonify
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Required


# Set up the app configuration.
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/api/<chatroom_name>', methods=['GET', 'POST'])
def chatroom_api(chatroom_name='Default'):
    """Retrieve all messages for a given chatroom via JSON REST API.
    """
    test_json = {
            "chatroom_name": "greg_and_dave",
            "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
            "members": ["Greg, David"],
            "messages": [
                {
                    "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                    "sender": "Greg",
                    "text": "Hi David!"
                },
                {
                    "date": datetime.strptime("2014-11-16", "%Y-%m-%d"),
                    "sender": "David",
                    "text": "Hey Greg!"
                }
            ],
        }
    return jsonify(**test_json)

if __name__ == '__main__':
    # Key probably shouldn't be kept in plain text in the code.
    app.secret_key = 'A4M5Ldse5nb88'
    app.run(debug=True)
