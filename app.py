from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/blacklist')
def blacklist():
    return render_template('blacklist.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

@app.route('/issues')
def issues():
    return render_template('issues.html')



if __name__ == '__main__':
    app.run(debug=False)