from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        sender = "purecoding@163.com"  # 发送方
        content = "用户名: "+request.POST['MERGE1']+"\n邮箱: "+request.POST['MERGE0']+"\n留言: "+request.POST['message']
        recver = "purecoding@163.com"  # 接收方
        password = "ZGWLAAOWKCTEKFNP"  # 邮箱密码
        message = MIMEText(content, "plain", "utf-8")
        message['Subject'] = f"用户提交数据"  # 邮件标题
        message['To'] = recver  # 收件人
        message['From'] = sender  # 发件人
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)  # 实例化smtp服务器
        smtp.login(sender, password)  # 发件人登录
        smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
        smtp.close()
    return render(request, 'main_page.html')
