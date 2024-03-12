from flask import Flask, render_template, request
import requests

application = Flask(__name__)

class Location:
    def __init__(self):
        self.address = "N/A"
        self.lat = 0
        self.lon = 0


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/submit', methods=['POST'])
def submit():
    location = Location()
    location.address = request.form['address']

    get_coordinates(location)

    return render_template('coords.html', lat = location.lat, lon = location.lon)


def get_coordinates(location):
    url = f'https://nominatim.openstreetmap.org/search?format=json&q={location.address}'
    response = requests.get(url)
    data = response.json()
    if data:
        locationInfo = data[0]
        location.lat = float(locationInfo['lat'])
        location.lon = float(locationInfo['lon'])
    else:
        location.lat = None
        location.lon = None

if __name__ == '__main__':
    application.run(debug=True)

    