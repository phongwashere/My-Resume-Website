import flask

app = flask.Flask(__name__)


@app.route('/')
def firstpage():
    return flask.render_template("index.html")

@app.route('/info')
def infopage():
    return flask.render_template("info.html")

@app.route('/DjKhaled')
def Khaledpage():
    return flask.render_template("DjKhaled.html")    

app.run(debug=True)