from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/songs')
def songs():
    return render_template('songs.html')

if __name__ == '__main__':
    app.run(debug=False)