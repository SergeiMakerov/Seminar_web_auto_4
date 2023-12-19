import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email():
    fromemail = "logsautotests@mail.ru"
    toaddr = "makerovs@yandex.ru"
    mypassword = "DkY5mbmXLwtc9mxxBMcj"
    reportname = "log.txt"

    msg = MIMEMultipart()
    msg['From'] = fromemail
    msg['To'] = toaddr
    msg['Subject'] = 'Hello from Python'

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
        msg.attach(part)

    body = "test Hello from Python"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromemail, mypassword)
    text = msg.as_string()
    server.sendmail(fromemail, toaddr, text)
    server.quit()


if __name__ == '__main__':
    send_email()
