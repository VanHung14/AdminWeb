import re
from sqlite3 import Time
from django.shortcuts import render
from django.views import View
from home.models import People,Account,CheckPeople
from home.form import PeopleForm
from django.contrib import messages
from django.http import HttpResponse
import math
# Create your views here.
def login(request):
    return render(request, "login/login.html")

def home(request):
    username = request.POST.get("username").strip()
    password = request.POST.get("password").strip()
    try:
        a = Account.objects.get(UserName=username, Password=password)
        p = People.objects.get(ID=a.people_id)
        request.session['people_id'] = p.ID
        request.session['role_id'] = p.RoleID
        q = People.objects.get(pk=p.ID)
        return render(request, 'home/index.html', {"people": q})
    except:
        return render(request, "login/login.html")

def logout(request):
    del request.session['people_id']
    del request.session['role_id']
    return render(request, "login/login.html")

def listUser(request):
    people = People.objects.all().order_by('ID')
    if(request.session['role_id']==1):
        return render(request, 'tablelist/index.html', {"people": people})
    return HttpResponse('Chuc nang nay chi danh cho admin')
    
    

def detailUser(request,people_id):
    #dulieu = request.POST['people_id']
    # print(people_id)
    q = People.objects.get(pk=people_id)
    return render(request, 'home/index.html', {"people": q})

def updateUser(request,people_id):
    list = People.objects.all().order_by("ID")
    updatePeople = People.objects.get(pk=people_id)
    name = request.POST.get("Name").strip()
    Gender = request.POST.get("Gender").strip()
    if(Gender == "Nam"): Gender = 1
    else: Gender = 0
    roleid = updatePeople.RoleID
    if(roleid == 1):
        RFID = request.POST.get("RFID").strip()
    else:
        RFID = updatePeople.RFID
    age = request.POST.get("Age").strip()

    # if (roleid == "User"):
    #     roleid = 0
    # else:
    #     roleid = 1
    context ={"ID":people_id,"Name":name,"Age":age,"Gender":Gender,"RFID":RFID,"RoleID":roleid}
    form = PeopleForm(context,instance= updatePeople)
    if form.is_valid():
        form.save()
        messages.success(request,"Thành công!")
        if (request.session['role_id'] == 1):
            return render(request, "tablelist/index.html", {"people": list})
        else:
            q = People.objects.get(pk=people_id)
            return render(request, 'home/index.html', {"people": q})
    else:
        return HttpResponse(f"Update không thành công")

def listNotification(request):

    if(request.session['role_id']):
        # lấy tất cả
        timerecord = CheckPeople.objects.all()
        print(1)
    else:
        timerecord = CheckPeople.objects.filter(id_check= request.session['people_id']).order_by('-time')
    list =[]
    for i in timerecord:
        if i.id_check == 0:
            list.append({"Name": "Không xác định", "Time": i.time, "checkpeople": i.checkpeople})
        else:
            p = People.objects.get(pk=i.id_check)
            list.append({"Name":p.Name,"Time":i.time,"checkpeople":i.checkpeople})
    return render(request, 'notification/notification.html', {"people": list})

def searchUser(request):
    try:
        strSearch = request.POST.get("strSearch").strip()
        people = People.objects.filter(Name__icontains=strSearch).order_by('ID')
        if (request.session['role_id'] == 1):
            return render(request, 'tablelist/index.html', {"people": people})
        # return HttpResponse('Chuc nang nay chi danh cho admin')
    except:
        return HttpResponse('Chuc nang nay chi danh cho admin')

def deleteUser(request, people_id):
    People.objects.filter(ID=people_id).delete()
    people = People.objects.all().order_by('ID')
    return render(request, 'tablelist/index.html', {"people": people})

def statistical(request):
    timesface = CheckPeople.objects.filter(checkpeople = 1).count()
    timesrfid = CheckPeople.objects.filter(checkpeople = 0).count()
    timestrueface = CheckPeople.objects.filter(checkpeople = 1, ok=1).count()
    timestruerfid = CheckPeople.objects.filter(checkpeople = 0, ok=1).count()
    percentface = round(timestrueface/timesface *100,2)
    percentrfid = round(timestruerfid/timesrfid *100,2)
    # print(statistical)
    return render(request,'statistical/statistical.html',{
        "timesface" : timesface,
        "timesrfid" : timesrfid,
        "timestrueface":timestrueface,
        "timestruerfid":timestruerfid,
        "percentface" : percentface,
        "percentrfid" : percentrfid
    })


