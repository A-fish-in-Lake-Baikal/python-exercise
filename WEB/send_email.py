# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

with open (r'E:\python\RC2.3.3\test_report\2018-05-17-14_30_42HTMLtemplate.html','r') as file:
    text = file.read()

from_addr = '3536046934@qq.com'
password = 'ilxhssalsnvpchjg'
to_addr = '3409256447@qq.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText("马维畅是你大爷",'plain', 'utf-8')
msg['From'] = _format_addr('你大爷的来信 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('马大爷', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()