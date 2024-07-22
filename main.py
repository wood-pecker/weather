from flask import Flask, render_template, request, redirect, url_for
from weather import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = get_weather(request.form['name'])
        if data['cod'] == 200:
            return render_template('weather.html', data=data)
        else:
            return '<h2>Check the entered data and try again!</h2>'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()