from flask import Flask


app = Flask(__name__)


@app.route('/')
def route_index():
    pass


@app.route('/request-counter')
def route_request_counter():
    pass


@app.route('/statistics')
def route_statistics():
    pass


if __name__ == '__main__':
    app.run(
        debug=True
    )