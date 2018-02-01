from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from mysite import models
# Create your views here.

def index(request):
    temp = []
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)

    #     if username == "shaw" and password == "1234":
    #         models.UserInfo.objects.create(user=username, pwd=password)
    #         print("login success")
    #         temp = {"word": "login success"}
    #     else:
    #         print("please enter correct username or password!")
    #         temp = {"word": "please enter correct username or password!"}
    # user_list=models.UserInfo.objects.all()
        result = models.UserInfo.objects.filter(user=username, pwd=password)
        print(result.values())
        if result:
#             return HttpResponseRedirect("/member/")
            return render(request, "member.html", {"user1": username})
        else:
            temp = {"word": "please enter correct username or password!"}
    return render(request, "index.html", {"data": temp})

def member(request):
    return render(request,"member.html")
