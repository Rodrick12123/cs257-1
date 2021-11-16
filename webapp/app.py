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

@app.route('/SpecificCups')
def page2():
    return flask.render_template('SpecificCups.html', results='Results')

@app.route('/AllCups')
def page3():
    return flask.render_template('AllCups.html', results='Results')
    
@app.route('/AllCups/Team')
def page4():
    return flask.render_template('OneTeamAllCups.html')

@app.route('/SpecificCups/Team')
def page5():
    return flask.render_template('OneTeamOneCup.html')

@app.route('/help/')
def help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Flask applications')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
