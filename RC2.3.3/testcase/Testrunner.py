# Testrunner方法
import unittest
import time
import os.path
import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


'''case = unittest.TestSuite()
case.addTest(Search('test_search1'))
case.addTest(Search('test_search2'))
case.addTest(MasterStation('test_log_in'))
case.addTest(MasterStation('test_home_page_assert'))
case.addTest(MasterStation('test_home_page_search'))
'''



# 查找最新的测试报告然后发送
def send_report():
    result_dir = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    lists = os.listdir(result_dir)

    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))

    print('最新文件为：' + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    print('绝对路径为：' + file)
    send_mail(file)

# 发送邮件的方法
def send_mail(newfile):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    with open(newfile,'rb') as file:
        text = file.read()
        # print('-------------------------------------------%s' % text)
    from_addr = '3536046934@qq.com'
    password = 'ilxhssalsnvpchjg'
    to_addr = '1627967707@qq.com'
    smtp_server = 'smtp.qq.com'

    msg = MIMEText(text, 'html', 'utf-8')
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
    #  设置报告文件保存路径  
    report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    #  获取系统当前时间  
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式  
    HtmlFile = report_path + now + "HTMLtemplate.html"
    fp = open(HtmlFile, "wb")

    # discover方法
    suite = unittest.TestLoader().discover('../testcase', pattern='test*.py')
    #执行用例  
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = u"RC2.3.3自动化测试报告",description = u"用例执行情况")
    runner.run(suite)
    fp.close()
    send_report()