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

@app.route('/SpecificCup')
def page2():
    return flask.render_template('OneCup.html', results='Results')

@app.route('/ManyCups')
def page3():
    return flask.render_template('ManyCups.html', results='Results')

@app.route('/OneCup')
def page4():
    return flask.render_template('OneCup.html', results='Results')

@app.route('/help/')
def help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Flask applications')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
