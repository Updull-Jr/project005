from flask import Flask

app = Flask(__name__)

@app.route("/", metghods = ['GET', 'POST'])
def index():
    return "starting ml project"

if __name__ == "__main__":
    app.run(debug=True)


