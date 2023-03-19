import flask

app = flask.Flask(__name__)


@app.route('/')
def firstpage():
    return flask.render_template("index.html")

@app.route('/certificates')
def certificatepage():
    return flask.render_template("certificates.html")

@app.route('/projects')
def projectspage():
    return flask.render_template("projects.html")    

app.run(debug=True)