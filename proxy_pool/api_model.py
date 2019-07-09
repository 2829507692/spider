from flask import Flask,g
from storage_model import RedisClient

app =Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis=RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h1> welcome to proxy pool system</h1>'


@app.route('/random')
def get_proxy():
    conn =get_conn()
    return  conn.random()

@app.route('/count')
def get_counts():
    conn =get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run()