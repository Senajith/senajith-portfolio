from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    message = request.form['message']
    
    # Send email
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Contact Form Submission'
    msg['From'] = email
    msg['To'] = 'senajithsrs@gmail.com'  # Replace with your email
    
    smtp = smtplib.SMTP('smtp.example.com')  # Replace with your SMTP server
    smtp.send_message(msg)
    smtp.quit()
    
    return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
