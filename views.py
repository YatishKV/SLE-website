from flask import Blueprint,render_template,request
import smtplib, ssl
import os
#from dotenv import dotenv_values
#config = dotenv_values(".env")

views=Blueprint(__name__,"views")

def send_email(name,phone_no,email,message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    #sender_email = config["USERNAME"]  # Enter your address
    receiver_email = email  # Enter receiver address
    #password = config["PASSWORD"]
    sender_email = os.environ.get("USERNAME")
    password = os.environb.get("PASSWORD")
    message = """\
    Sri Lakshmi Enterprices

    This is a copy of the message sent from {} to Sri Lakshmi enterprices.
    phone_no : {}
    email : {}
    message: {}""".format(name,phone_no,email,message)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except: pass

@views.route("/")
def home():
    args = request.args
    if len(args)>0:    
        if args['Name'] and args['PhoneNumber'] and args['Email'] and args['Message']:
            name = args.get('Name')
            phone_no = args.get('PhoneNumber')
            email = args.get('Email')
            message = args.get('Message')
            send_email(name,phone_no,email,message)
            
    return render_template("index.html")