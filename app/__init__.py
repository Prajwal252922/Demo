"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq2jg2qv2dcb92e0i0-a.singapore-postgres.render.com",
        database="demo_4fkn",
        user="prajwal",
        password="euim6On2VzfOenXNVc31qG8UYa8yN4g4")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
