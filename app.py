import os
import dotenv
import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/quotes"

def fetch_quote():
    headers = {"X-Api-Key": API_KEY}
    try:
        # We don't specify a category to get a wider variety of quotes
        response = requests.get(API_URL, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()[0]
    except Exception as e:
        print(f"Error: {e}")
    
    # High-quality fallback if API fails
    return {
        "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill",
        "category": "Motivation"
    }

@app.route('/')
def index():
    initial_quote = fetch_quote()
    return render_template('ai.html', quote=initial_quote)

@app.route('/api/new-quote')
def new_quote():
    data = fetch_quote()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)