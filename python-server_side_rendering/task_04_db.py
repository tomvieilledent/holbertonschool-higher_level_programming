#!/usr/bin/python3
"""Flask app: display products from JSON, CSV or SQLite (source=query param)."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [{
                'id': int(r['id']),
                'name': r['name'],
                'category': r['category'],
                'price': float(r['price'])
            } for r in reader]
    except FileNotFoundError:
        return []


def read_sqlite(db_path='products.db'):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute('SELECT id, name, category, price FROM Products')
        rows = cur.fetchall()
        return [
            {'id': row['id'], 'name': row['name'],
                'category': row['category'], 'price': row['price']}
            for row in rows
        ]
    finally:
        conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    prod_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            products = read_json()
        elif source == 'csv':
            products = read_csv()
        else:  # sql
            products = read_sqlite()
    except FileNotFoundError as e:
        return render_template('product_display.html', error=str(e))
    except sqlite3.Error as e:
        return render_template('product_display.html', error=f'Database error: {e}')

    if prod_id:
        try:
            pid = int(prod_id)
        except ValueError:
            return render_template('product_display.html', error='Invalid id')
        products = [p for p in products if int(p.get('id', 0)) == pid]
        if not products:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
