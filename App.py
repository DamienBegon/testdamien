import flask

app = flask.Flask(__name__)

@app.route('/')
def app():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)