import smtplib, ssl

SENDER_EMAIL    = 'craigrobson74@gmail.com'  # replace with your email address
SENDER_PASSWORD = 'fgk2idfgk2id'             # replace with your email password
SENDER_PASSWORD = 'swcglrsttkbaxels'

def send_mail(receiver_email, subject, body):
  port    = 465
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context ) as server:
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail( SENDER_EMAIL, receiver_email, body )

send_mail( 'carobson652@yahoo.com', 'Subject1', 'How are you today?')
send_mail( 'carobson652@gmail.com', 'Subject1', 'How are you today?')