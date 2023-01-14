import random
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/<int:id>/<int:max>")
def out(id,max):
    return str(random.randrange(id,max))

if __name__ == "__main__":
    app.run(debug=True)
