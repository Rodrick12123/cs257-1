'''
    app.py
    Rodrick and Thea
'''
import argparse
import flask
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/mockup1')
def page1():
    return flask.render_template('mockup1.html')

@app.route('/mockup2')
def page2():
    return flask.render_template('mockup2.html')

@app.route('/mockup3')
def page3():
    return flask.render_template('mockup3.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Flask applications')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)