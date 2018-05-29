# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def send_maile():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    with open (r'html_1.html','rb') as file:
        text=file.read()
        print('-------------------------------------------%s' %text)
    from_addr = '3536046934@qq.com'
    password = 'ilxhssalsnvpchjg'
    to_addr = 'mawc@parasaga.com'
    smtp_server = 'smtp.qq.com'

    msg = MIMEText(text,'html', 'utf-8')
    msg['From'] = _format_addr('tester <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('自动化测试报告', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__=='__main__':
    send_maile()