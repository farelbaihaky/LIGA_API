from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

headers_premier_league = {
    "X-RapidAPI-Key": "257bf38cfamshf91c48194aa6c72p16f38bjsn3026d017602c",
    "X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
}

premier_league_url = "https://premier-league-standings1.p.rapidapi.com/"

headers_laliga = {
    "X-RapidAPI-Key": "257bf38cfamshf91c48194aa6c72p16f38bjsn3026d017602c",
    "X-RapidAPI-Host": "laliga-standings.p.rapidapi.com"
}

laliga_url = "https://laliga-standings.p.rapidapi.com/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_data', methods=['POST'])
def select_data():
    selected_data = request.form.get('data')
    if selected_data == 'premier_league':
        data = fetch_data(premier_league_url, headers_premier_league)
        return render_template('premier_league.html', premier_league_data=data)
    elif selected_data == 'laliga':
        data = fetch_data(laliga_url, headers_laliga)
        return render_template('laliga.html', laliga_data=data)
    else:
        return "Invalid selection."

def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/premier_league_data')
def premier_league_data():
    data = fetch_data(premier_league_url, headers_premier_league)
    return render_template('premier_league.html', premier_league_data=data)

@app.route('/laliga_data')
def laliga_data():
    data = fetch_data(laliga_url, headers_laliga)
    return render_template('laliga.html', laliga_data=data)

if __name__ == '__main__':
    app.run(debug=True)