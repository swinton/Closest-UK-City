from flask import Flask, jsonify
app = Flask(__name__)

from closest_city import closest_city

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_closest_city/<lat>/<lng>')
def get_closest_city(lat, lng):
    city, city_lat, city_lng, dist = closest_city(float(lat), float(lng))
    return jsonify(city=city, city_lat=city_lat, city_lng=city_lng, dist=dist)

if __name__ == '__main__':
    app.run()