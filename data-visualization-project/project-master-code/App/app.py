from flask import Flask, jsonify, request, render_template

import sys
sys.path.append("./playtime_pred")
sys.path.append("./sales_pred")
import PlaytimePrediction as Playtime
import SalesPrediction as Sales

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/playtime', methods=['GET'])
def get_playtime():
    args = request.args

    genre = args['genre']
    content_rating = args['content_rating']
    platform = args['platform']
    price = args['price']

    results = Playtime.predict_playtime(genre, content_rating, platform, price)

    return jsonify(results)

@app.route('/sales', methods=['GET'])
def get_sales():
    args = request.args

    region = args['region']
    year_since_release = args['year_since_release']
    expected_rating = args['expected_rating']
    is_top_publisher = args['is_top_publisher']

    results = Sales.predict_sales(region, year_since_release, expected_rating, is_top_publisher)

    return jsonify(results)

@app.route('/all_sales', methods=['GET'])
def get_all_sales():
    args = request.args

    expected_rating = args['expected_rating']
    is_top_publisher = args['is_top_publisher']

    results = Sales.predict_all_sales(expected_rating, is_top_publisher)

    return jsonify(results)

# prevent cached responses
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8001, debug=True)

app.run(host='127.0.0.1', port=8001, debug=True)