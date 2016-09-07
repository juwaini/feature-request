from flask import Flask, url_for, render_template
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

if __name__ == '__main__':
    app.run()
