import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message:
    def send_message(self, login, password, subject, message, recipients, gmail_smtp):
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(login, password)
        ms.sendmail(login, ms, msg.as_string())

        ms.quit()
        #send end

    def recieve_message(self, login, password, gmail_imap, header):
        mail = imaplib.IMAP4_SSL(gmail_imap)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        #end recieve

if __name__ == '__main__':
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    m = Message()
    m.send_message(login, password, subject, message, recipients, gmail_smtp)
    m.recieve_message(login, password, gmail_imap, header)
