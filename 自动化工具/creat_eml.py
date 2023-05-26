from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gen_Emails(object):
    def __init__(self):
        self.EmailGen()

    def EmailGen(self):
        sender = 'sender'
        recepiant = 'recipiant'
        subject = 'subject'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recepiant


        html = """\
        <html>
            <head></head>
            <body>
                <p> hello world </p>
            </body>
        </html>
        """
        part = MIMEText(html, 'html')

        msg.attach(part)
        msg.add_attatchment()

        self.SaveToFile(msg)

    def SaveToFile(self,msg):
        out_file = active_dir
        with open(out_file,'w') as out_file:
            gen = generator.Generator(out_file)
            gen.flatten(msg)

if __name__=='__main__':
    for i in range(10):
        active_dir = 'D:\\{}.eml'.format(i)
        eml = Gen_Emails()