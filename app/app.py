# Import flask module
from flask import Flask

# create an app instance
app = Flask(__name__)

# end point
@app.route("/")
def helloDragon():
    return "Welcome to Dragon Fly!!!"


# running python app.py
if __name__ == "__main__":
    app.run(debug=True)