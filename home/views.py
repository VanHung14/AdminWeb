from django.shortcuts import render
from django.views import View
from home.models import People,Account,TimeRecord
from home.form import PeopleForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, "login/login.html")

def home(request):
    username = request.POST.get("username").strip()
    password = request.POST.get("password").strip()
    a = Account.objects.get(UserName=username)
    p= People.objects.get(ID=a.people_id)
    print(1)
    if (a):
        if(password == a.Password):
            request.session['people_id'] = p.ID
            if(p.RoleID == 1):
                people = People.objects.all().order_by('ID')
                return render(request, 'tablelist/index.html', {"people": people})
            else:
                return render(request, 'home/index.html', {"people": p})
    return render(request, "login/login.html")

def logout(request):
    del request.session['people_id']
    return render(request, "login/login.html")

def listUser(request):
    people = People.objects.all().order_by('ID')
    return render(request, 'tablelist/index.html', {"people": people})

def detailUser(request,people_id):
    #dulieu = request.POST['people_id']
    print(people_id)
    q = People.objects.get(pk=people_id)
    return render(request, 'home/index.html', {"people": q})

def updateUser(request,people_id):
    list = People.objects.all().order_by("ID")
    updatePeople = People.objects.get(pk=people_id)
    name = request.POST.get("Name").strip()
    Gender = request.POST.get("Gender").strip()
    if(Gender == "Nam"): Gender = 1
    else: Gender = 0
    RFID = request.POST.get("RFID").strip()
    age = request.POST.get("Age").strip()
    roleid = updatePeople.RoleID
    if (roleid == "User"):
        roleid = 0
    else:
        roleid = 1
    context ={"ID":people_id,"Name":name,"Age":age,"Gender":Gender,"RFID":RFID,"RoleID":roleid}
    form = PeopleForm(context,instance= updatePeople)
    if form.is_valid():
        form.save()
        messages.success(request,"Thành công!")
        return render(request, "tablelist/index.html", {"people": list})
    else:
        return HttpResponse(f"Update không thành công")

def listNotification(request):
    timerecord = TimeRecord.objects.all()
    list =[]
    for i in timerecord:
        p = People.objects.get(pk=i.people_id)
        list.append({'ID':p.ID,"Name":p.Name,"Age":p.Age,"Time":i.time})
        print(i.time)
    return render(request, 'notification/notification.html', {"people": list})
