import time
import math
from typing import NewType
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.shortcuts import redirect
from user.models import comment, post, postphotos ,postbody
from user.models import comment
from django.core.files.storage import FileSystemStorage
from PIL import Image
from user.models import postbody
# def create_posts(request):
#     pos_=None
#     body=str(request.POST.get('body'))
#     meta_body=str(body[0:50])
#     print(meta_body)
#     print(request.POST)
#     if request.FILES:
#         upload_file=request.FILES['image']

#         pos_=post(user=request.user,title=request.POST.get('title'),body=request.POST.get('body'),meta_body=meta_body,image=upload_file)
#     else:
#         pos_=post(user=request.user,title=request.POST.get('title'),body=request.POST.get('body'),meta_body=meta_body)
#     pos_.save()
#     return 0

def create_post_body(pos,body):
    p_id = int()
    newbody = postbody(user = pos,body = body)
    newbody.save()
    p_id = newbody.id
    return p_id

def create_post_photo(pos,FILE):
    photo_id = int()
    new_photo = postphotos(user=pos,image=FILE)
    new_photo.save()
    photo_id = new_photo.id
    return photo_id

def create_posts(request):
    pos_=None
    body=str(request.POST.get('body'))
    
    NEW_POST = post(user = request.user,title=request.POST.get('title'),meta_body=str(),body=str())
    NEW_POST.save()
    I_ID = list()
    final_str = list()
    ll = list()
    if request.FILES:
        j = 0
        while j>= 0:
            pb = create_post_body(NEW_POST,body[j:body.find('IMAGE',j)])
            print(body[j:body.find('IMAGE',j)])   
            txt ="txt_"+ str(pb)
            final_str.append(txt)
            ll.append(body[j:body.find('IMAGE',j)])
            j = body.find('IMAGE',j)            
            if j<0:
                break
            img_id = body[j+6:j+7]
            
            #IMAGE
            url='image'+str(int(img_id))
            pi = postphotos(user=NEW_POST,image = request.FILES[url])
            pi.save()
            I_ID.append(pi.id)
            #body
            
            print()
            imf = "img_"+ str(int(pi.id))
            final_str.append(imf)

            j=j+8
        print(final_str)
        j=0
        d=dict()
        for i in final_str:
            d[j]=i
            j+=1
        print(d)
        import json
        NEW_POST.body = json.dumps(d)
        NEW_POST.image = postphotos.objects.all().filter(id = int(I_ID[0])).first().image
        NEW_POST.meta_body = ll[0]
        NEW_POST.save()



        return 

    else:
        return
    

def get_all_data(request):
    post_method_data=request.POST
    get_mehtod_data = request.GET
    post_id=get_mehtod_data.get('post_id')#it willl supply the data from the html form and give us the post id
    post_info = post.objects.all().filter(id=post_id).first()
    #print(post_info)
    all_comments = comment.objects.all().filter(key=post_info)
    cmnt_dict = list()
    from django.contrib.auth.models import User
    for i in all_comments:
        if not i.user == 'None':
            user = User.objects.all().filter(id=int(i.user)).first()
        else:
            user = 'Anoymous'
        cmnt_dict.append( {'comment':i,'auth':user})

    #print('all_comments:',all_comments)
    all_data={'post':post_info,'comments':cmnt_dict}
    return all_data

#d2c3963f29d3.ngrok.io


def process_post_body(body=str()):
    import json
    result = list()
    dic1 = json.loads(body)
    # a = postbody.objects.all().filter(id=1)
    print('body',dic1) 
    for i,j in dic1.items():
        key = j[:4]
        value = j[4:len(j)]    
        print(key)
        print(value)
        if key == "txt_":
            a = postbody.objects.all().filter(id=int(value)).first()
            # print(a.body)
            result.append({'text':True,'content':a})
        if key == "img_":
            a = postphotos.objects.all().filter(id=int(value)).first()
            # print(a.body)
            result.append({'image':True,'url':a})
    return result


def make_comment(request,data0):
    from user.models import comment as cmnt
    # print(request.POST)
    data = request.POST
    print(request.user)

    if not request.user.is_authenticated:
        print('none')
        new_cmnt = comment(key=data0['post'],comment_body = data['body'],is_auth = False,user='None')
        new_cmnt.save()
        return
    else:
        print('data',data0)
        if request.user == data0['post'].user:
            new_cmnt = comment(key=data0['post'],user=str(request.user.id),comment_body = data['body'],is_auth = True)
            new_cmnt.save()
        else:
            print('he is not the auth')
            new_cmnt = comment(key=data0['post'],comment_body = data['body'],is_auth = False,user=request.user.id)
            new_cmnt.save()
    return












