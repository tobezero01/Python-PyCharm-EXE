import pyodbc
import flask
from Config import conn_str
from SQLQuery import *
# kết nối
try:
    conn = pyodbc.connect(conn_str)
    #methods: GET: select, POST: insert, PUT: update
    app = flask.Flask(__name__)
    
    if __name__ == "__main__":
        app.run(port = 3333)
except Exception as e:
    print(e)
