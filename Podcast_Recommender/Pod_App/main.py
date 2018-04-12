from flask import Flask, request, render_template
from py_podcasts import podcast_recommendations
import pickle
import pandas as pd
from io import BytesIO
import os

pods = pd.read_pickle('pod_df.gz', compression='gzip')

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /recommend_podcasts page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/recommend_podcasts/', methods=['GET', 'POST'])

def render_message():

    # error messages to ensure correct units of measure
    error = "YOU MUST ENTER A PODCAST FOUND IN THE SEARCHBAR"

    # hold all amounts as floats
    podcast = request.form["user_podcast"]

    # # takes user input and ensures it can be turned into floats
    #
    # user_input = input.typeahead.tt-query.tt-input
    # print(type(user_input))
#         try:
#             float_feature = float(user_input)
#         except:
#             return render_template('index.html', message=messages[i])
    # inputs.append(user_input)
    if podcast not in list(pods.Podcast):
        return render_template('index.html', message=error)

    else:
    # show user final message
        final_message = podcast_recommendations(podcast)
        return render_template('index.html', message=final_message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
