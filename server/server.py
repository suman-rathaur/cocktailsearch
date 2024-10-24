# Flask app (server.py)
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin  # Make sure you import cross_origin
import util

app = Flask(__name__)
CORS(app)  # Apply CORS to the entire app
util.load_saved_artifacts()

# Function to search for top 3 bars based on the cocktail
@app.route('/search', methods=['GET', 'POST'])  # Allow both GET and POST
def search_cocktail():
    cocktail_name = request.form['cocktail']
    #cocktail_name = request.args.get('cocktail', '').title()  # Get cocktail name from query
    #bars = util.search_cocktail(cocktail_name)  # Fetch bars from util function
    # response = jsonify({
    #     'bars': bars
    # })
    response = jsonify({
            'estimated_bar': util.search_cocktail(cocktail_name)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Searching Cocktails...")
    app.run()