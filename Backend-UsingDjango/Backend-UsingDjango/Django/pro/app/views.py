
from email import message
import email
from django.contrib import messages
from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from pro import settings
from django.core.mail import send_mail
from PIL import Image
from .models import Upload
import img2pdf 
from PIL import Image 
import os
# Create your views here.

def home(request):
    if request.method== "POST":
        file=request.FILES['upfiles']
        document=Upload.objects.create(file=file)
        document.save()
        return render(request,'file.html')
        # return HttpResponse('File is Uploaded')
    return render(request,'index.html')

#-------------------------------------- Image to Pdf ------------------------#

# image_1 = Image.open(r'media/0x0.jpg')
# im_1 = image_1.convert('RGB')
# im_1.save(r'media/new.pdf')
# output 
 
def render_file(request):
    if request.method== "GET":
        
        doc=Upload.objects.create(file)
        image_1 = Image.open(r'media/0x0.jpg')
        im_1 = image_1.convert('RGB')
        im_1.save(r'media/new1.pdf')
        doc.save()
        
        print('file is converted')
        # return HttpResponse('File Converted')

def signup(request):
    if request.method== "POST":
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        if User.objects.filter(email=email):
            messages.error(request,"Email already exist!")
            return redirect('home')
        
        if pass1!=pass2:
            messages.info(request,'Password didnt match')
            return redirect('home')





        myuser=User.objects.create_user(email,pass1,pass2)
        myuser.email=email
        myuser.pass1=pass1
        myuser.pass2=pass2
        myuser.save()

        
        #welcome email

        subject="Welcome to DocNest"
        message="Hello and Thank you for creating account in DocNest,\n We have Sent you a confirmation E-mail, So please verify It"
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        # messages.__str__(request, "Your")
        





    return render(request, 'signup.html')
def login(request):
    if request.method== "POST":
        email=request.POST['email']
        password=request.POST['pass']
        user=authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            return redirect('home')
    return render(request,'login.html')
def logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    
    return redirect('home')
    

def aboutus(request):
    return render(request, 'about_us.html')    
