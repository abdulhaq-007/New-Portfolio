from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import telebot
TOKEN = '5159636314:AAHMaQQG5PgTVZUFkUtGUYMKQ9i1kUgUWJ8'
bot = telebot.TeleBot(TOKEN)
user = "1006979245"
# Create your views here.

def homeView(request):
    return render(request, 'index.html')

def aboutView(request):
    return render(request, 'about.html')

def portfolioView(request):
    return render(request, 'portfolio-details.html')        

def servicesView(request):
    return render(request, 'services.html') 

def resumeView(request):
    return render(request, 'resume.html') 

def contactView(request):
    if request.GET:
        bot.send_message(user, f"Portfolio \n Name:{request.GET['name']} \n Email:{request.GET['email']} \n Message: {request.GET['message']}")
        return redirect('/contact') 
    return render(request, 'contact.html')

def portView(request):
    return render(request, 'portfolio.html')    

           