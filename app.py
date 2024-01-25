from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ronaldo Roymundus Gultom, 2101160002, Teknologi Informasi!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
