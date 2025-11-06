from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # for flashing messages

# -------------------- MAIL CONFIG --------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'myy502388@gmail.com'       # your Gmail
app.config['MAIL_PASSWORD'] = ''     # use an app password
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'my502388@gmail.com')

mail = Mail(app)
# ------------------------------------------------------

# -------------------- ROUTES --------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            msg = Message(subject=f"New Contact: {subject}",
                          recipients=['myy502388@gmail.com'])  # Where you receive the message
            msg.body = f"""
You have a new message from your portfolio contact form:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
            mail.send(msg)
            flash("✅ Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending message: {e}", "danger")

        return redirect(url_for('contact'))

    return render_template('contact.html')
# ------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
