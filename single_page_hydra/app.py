import sys
from flask import (
    Flask,
    render_template,
    request,
)

# Need to add the project directory to the path to fix the ImportError.
sys.path.append('..')

from single_page_hydra.api.manager import ApiManager

app = Flask(__name__)
api_manager = ApiManager()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')
    return render_template('search.html', query=search_query)


@app.route('/search_results', methods=['POST'])
def search_results():
    search_query = request.form.get('query')
    results = api_manager.search(search_query)
    return render_template('search_results.html', results=results, search=search_query)

if __name__ == '__main__':
    app.run(debug=True)
