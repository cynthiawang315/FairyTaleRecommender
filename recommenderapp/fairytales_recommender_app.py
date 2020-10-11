import flask
from flask import request
from fairytales_recommender_app_api import make_recommendation

# Initialize the app
app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
# @app.route("/")


@app.route("/", methods=["POST", "GET"])
def recommend():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    x_userinput, recommendation = make_recommendation(request.args)
    print(x_userinput)
    return flask.render_template('fairytale_recommender.html',
                                 x_userinput=x_userinput,
                                 recommendation=recommendation)




# For local development:
if __name__ == '__main__':
    app.run(debug=False)
