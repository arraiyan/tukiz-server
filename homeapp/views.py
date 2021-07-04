from user.models import post
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from .additionals import *
from django.core.files.storage import FileSystemStorage
from user.models import *
import json
# Create your views here.
def home_page(request):
    post_data=post.objects.all()
    context={'posts': post_data}#all the post from data base
    return render(request,'homeapp/index.html',context)



def create_post(request):
    if request.user.is_authenticated:
                if request.method=='POST':                  
                    create_posts(request)
                    print(request.FILES)
                    return redirect('home_page')
        
    else:
        
        return redirect('login')
    return render(request,'homeapp/post.html',None)



def blog_view(request):
    get_request_data=request.GET
    print(get_request_data)
    data = get_all_data(request)#INITIAL PROJECT DATA
    body = process_post_body(data['post'].body)#INITIAL DATA
    if request.method=='POST' and request.POST.get('class') == "comment":
        make_comment(request,data)
    data = get_all_data(request)
    body = process_post_body(data['post'].body)
    return render(request,'homeapp/blog_view.html',{'data':data,'body':body})








