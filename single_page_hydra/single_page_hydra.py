from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')
    return render_template('search.html', query=search_query)


if __name__ == '__main__':
    app.run(debug=True)
