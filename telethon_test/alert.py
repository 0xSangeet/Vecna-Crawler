import smtplib

def send_alert(email):
    try:
        sender_email = 'trapking9997@gmail.com'
        receiver_email = email
        subject = "URGENT! Email Leaked"
        message = "Your email has been found in a data breach. Please change your password as soon as possible.\n\n\nTeam VecnaCrawler :)"
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, "bcnfzynkfhqouegg")
        server.sendmail(sender_email, receiver_email, text)
    except:
        print("Failed to send email.")