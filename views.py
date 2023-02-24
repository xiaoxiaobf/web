from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText


# Create your views here.
def main_page(request):
    if request.method == 'POST':
        print('test')
    return render(request, 'main_page.html')
