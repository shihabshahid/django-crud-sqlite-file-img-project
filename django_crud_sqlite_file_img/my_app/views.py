import datetime
import os
from django import apps
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_table

# Create your views here.
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def retrieve(request):
    Context={
        'datas':user_table.objects.all()
    }
    return render(request,"retrieve.html",Context)

def create(request):
    if request.method=='POST':
        input_name = request.POST.get('name','')
        input_contact = request.POST.get('contact','')
        input_file = request.FILES['file']
        if input_file and allowed_file(input_file.name):
            user = user_table(name=input_name,contact=input_contact,filename=input_file)
            user.save()
            messages.success(request, 'Data Saved')
            return redirect('retrieve_url')       
        else:
            messages.warning(request, 'File formate must be png, jpg, jpeg and gif')
            return render(request,"create.html")
    elif request.method=='GET':
        return render(request,"create.html")
    
def update(request,id):
    user_data = user_table.objects.get(id=id)
    if request.method=='POST':
        user_data.name = request.POST.get('name','')
        user_data.contact = request.POST.get('contact','')
        if len(request.FILES) != 0:
            user_data.filename = request.FILES['file']
            if user_data.filename and allowed_file(user_data.filename.name):
                user_data.save()
                messages.success(request, 'Data Updated')
                return redirect('retrieve_url')
            else:
                messages.warning(request, 'File formate must be png, jpg, jpeg and gif')
                return redirect('retrieve_url')
        else:
            user_data.save()
            messages.success(request, 'Data Updated')
            return redirect('retrieve_url')
    elif request.method=='GET':
        Context={
            'datas':user_data
        }
        return render(request,"update.html",Context)
    
def delete(request,id):
    user_table.objects.get(id=id).delete()
    messages.success(request, 'Data Deleted')
    return redirect('retrieve_url')

