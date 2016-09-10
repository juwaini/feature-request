from flask import Flask, url_for, render_template, request, jsonify
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    panels = (
            {'href': 'feature-request', 'text': 'Feature Request', 'theads': ['date', 'title', 'requester', 'priority']},
            {'href': 'discussions', 'text': 'Discussions', 'theads': ['date', 'title', 'requester', 'priority', 'status']},
            )

    return render_template('index.html', panels=panels)

@app.route('/login')
def login():
    return 'Please login'

@app.route('/feature-requests', methods=['GET', 'POST'])
def feature_requests():
    if request.method == 'GET':
        fr = FeatureRequest()
        retval = {'no-of-feature-requests': fr.query.count()}
        return jsonify(retval), 200

if __name__ == '__main__':
    app.run(debug=True)
