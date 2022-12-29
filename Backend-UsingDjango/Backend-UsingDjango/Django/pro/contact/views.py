from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact(request):
    # messages.success(request,'Welcome to Contact')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        

        if len(name)<2 or len(email)<5:
            messages.error(request,"Please Fill The form correctly")
        else:
            contact=Contact(name=name,email=email,subject=subject,content=message)
            contact.save()
            messages.success(request,"Your Query is submitted")

    return render(request,'contact.html')