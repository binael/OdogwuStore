from api import mail
from flask_mail import Message
from threading import Thread
from flask import current_app
from uuid import uuid4

def send_async_email(app, msg):
    """_summary_

	Args:
		app (_type_): _description_
		msg (_type_): _description_
	"""
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    """_summary_

	Args:
		subject (_type_): _description_
		sender (_type_): _description_
		recipients (_type_): _description_
		html_body (_type_): _description_
	"""
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    # Use current_app._get_current_object() within the with block
    with current_app.app_context():
        Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()


def subscribe_mail(recipients):
    subject = "O-STORE: SUBSCRIPTION SUCCESSFUL"
    # Format the HTML body string with the firstname variable
    html_body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscription Confirmation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
		.header {
            text-align: center;
        }

        .header img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }

        .confirmation-section {
            max-width: 900px;
            margin: 40px auto;
            background-color: #fff;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .confirmation-title {
            font-size: 24px;
            color: #333;
            margin-bottom: 10px;
        }

        .confirmation-text {
            font-size: 15px;
            color: #888;
            line-height: 1.6;
        }
    </style>
</head>
<body>

    <div class="confirmation-section">
      	<div class="header">
			<img src="https://res.cloudinary.com/dael/image/upload/f_auto,q_auto/v1/o-store/gvpkyrytrgj3gshlqqjt" alt="Header Image">
		</div>
        <h2 class="confirmation-title">Thank You for Subscribing!</h2>
        <p class="confirmation-text">You have successfully subscribed to receive the latest updates and news from our ecommerce platform. We appreciate your interest and support. Keep an eye on your inbox for future updates.</p>
    </div>
</body>
</html>
"""
    send_email(subject=subject, sender="O-STORE", recipients=recipients, html_body=html_body)

def contact_us_mail(content):
    subject = "O-STORE: REQUEST RECEIVED"
    html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Enquiry Confirmation</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }}

        .confirmation-section {{
            max-width: 900px;
            margin: 40px auto;
            background-color: #fff;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .confirmation-title {{
            font-size: 24px;
            color: #333;
            margin-bottom: 10px;
        }}

        .confirmation-text {{
            font-size: 15px;
            color: #888;
            line-height: 1.6;
        }}

        .contact-details {{
            font-size: 14px;
            color: #888;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="confirmation-section">
        <h2 class="confirmation-title">Contact Enquiry Confirmation</h2>
        <p class="confirmation-text">We have received your contact enquiry. One of our team members will get back to you soon. In the meantime, here is a copy of your enquiry details:</p>
        <p class="contact-details">Enquiry ID: <span id="uuid">{str(uuid4())}</span></p>
        <p class="contact-details">First Name: <span id="firstName">{content.get('firstname')}</span></p>
        <p class="contact-details">Last Name: <span id="lastName">{content.get('lastname')}</span></p>
        <p class="contact-details">Email: <span id="email">{content.get('email')}</span></p>
        <p class="contact-details">Subject: <span id="subject">{content.get('topic')}</span></p>
        <p class="contact-details">Enquiry: <span id="enquiry">{content.get('description')}</span></p>
    </div>
</body>
</html>
"""
    send_email(subject=subject, sender="O-STORE", recipients=[content.get('email')], html_body=html_body)
