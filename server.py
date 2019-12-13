from flask import Flask, render_template, request
import data_manager

get_counter = 0
post_counter = 0
put_counter = 0
delete_counter = 0

req = {'GET': get_counter,
       'POST': post_counter,
       'PUT': put_counter,
       'DELETE': delete_counter}

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_request_counter():
    global get_counter
    get_counter += 1
    if request.method == 'POST':
        global post_counter
        post_counter += 1
        req.update({'POST': post_counter})
    if request.method == 'PUT':
        global put_counter
        put_counter += 1
        req.update({'PUT': put_counter})
    if request.method == 'DELETE':
        global delete_counter
        delete_counter += 1
        req.update({'DELETE': delete_counter})
    req.update({'GET': get_counter})
    data_manager.write_to_file('request_counter.txt', req)
    return render_template('request_counter.html')


@app.route('/statistics')
def route_statistics():
    return render_template('statistics.html',
                           get_counter=get_counter,
                           post_counter=post_counter,
                           put_counter=put_counter,
                           delete_counter=delete_counter
                           )


if __name__ == '__main__':
    app.run(
        debug=True
    )
