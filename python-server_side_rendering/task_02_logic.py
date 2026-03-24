#!/usr/bin/python3

from flask import Flask, render_template
import json
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    base_dir = Path(__file__).resolve().parent
    items_path = base_dir / 'items.json'
    with open(items_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    item = data.get('items', [])
    return render_template('items.html', items=item)


if __name__ == '__main__':
    app.run(debug=True, port=5050)
