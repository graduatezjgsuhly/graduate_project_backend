from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from users.models import Users
import json
# Create your views here.
def listusers(request):
    if request.method == 'GET':
        request.params = json.loads(request.body)
        id = request.params['id']
        try:
            select_user = Users.objects.get(id = id)
            print(select_user.passwd)
        except Users.DoesNotExist:
            return{
                'ret':1,
                'msg':"数据不存在"
            }
        #返回一个queryset对象 ,包含所有的表记录
        # qs = Users.objects.values()
        # # 每条表记录都是是一个dict对象，
        # # key 是字段名，value 是 字段值 
        # retStr = ''
        # for users in qs :
        #     print(users)    
        #     print(users['id'],)
        #     retStr += users['name'] + '|' + users['phonenumber']
        #     print(retStr)
        return JsonResponse({"ret":0})
def user_sign_up(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        info = request.params['data'] 
        print(info)
        new_user = Users.objects.create(
            phonenumber = info['phonenumber'],
            name = info['name'],
            passwd = info['passwd']
        ) 
        print("success")
        return JsonResponse({"ret": 0 , "id":new_user.id})
    else:
        return JsonResponse({"ret": 1})
def user_login_in(request):
    if request.method == 'GET':
        request.params = json.loads(request.body)
        
        print(request.params)
        id = request.params['id']
        passwd = request.params['passwd']
        try:
            select_user = Users.objects.get(id = id)
            if(select_user.passwd == passwd):
                return JsonResponse({
                    "ret" : 0
                })
            else:
                return JsonResponse({
                    'ret' : 1,
                    'msg' : "error"
                })
        except User.DoesNotExist:
            return{
                'ret':1,
                'msg':"数据不存在"
            }