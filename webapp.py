#!/usr/bin/env python

"""
Simple web app to return the closest UK city to a set of co-ordinates.
"""

from flask import Flask, jsonify

from closest_city import closest_city

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_closest_city/<lat>/<lng>')
def get_closest_city(lat, lng):
    city, city_lat, city_lng, dist = closest_city(float(lat), float(lng))
    return jsonify(city=city, city_lat=city_lat, city_lng=city_lng, dist=dist)

if __name__ == '__main__':
    app.run()