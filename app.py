import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Harumi Booth in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://hello_word_database_user:9JMau27WnwffUfKOeKY3K2jjBvSbbAPL@dpg-d23rne6mcj7s739mn3sg-a/hello_word_database")
    conn.close()
    return "Database Connection Successful"
