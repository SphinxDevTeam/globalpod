from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key

# Email configuration
SMTP_SERVER = "your-smtp-server"
SMTP_PORT = 587
SMTP_USERNAME = "rho-9@rho-9.com"
SMTP_PASSWORD = "your-email-password"

# Routes
@app.route('/')
def index():
    return render_template('index.html')

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
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        userid = request.form.get('userid')
        reason = request.form.get('reason')
        appeal = request.form.get('appeal')
        consent = request.form.get('consent')

        if not all([email, username, userid, reason, appeal, consent]):
            return "All fields are required", 400

        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = SMTP_USERNAME
            msg['To'] = SMTP_USERNAME  # Sending to ourselves
            msg['Subject'] = f"Blacklist Appeal from {username}"

            body = f"""
            Blacklist Appeal Submission:
            
            Email: {email}
            Discord Username: {username}
            Discord UserID: {userid}
            
            Blacklist Reason:
            {reason}
            
            Appeal:
            {appeal}
            
            Consent Given: Yes
            """

            msg.attach(MIMEText(body, 'plain'))

            # Send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)

            return redirect(url_for('contact_success'))
        except Exception as e:
            print(f"Error sending email: {e}")
            return "Error submitting form", 500

    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)