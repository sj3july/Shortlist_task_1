from multiprocessing import context
from django.shortcuts import render,HttpResponse
from HOME.models import Contact, Contact_1
# Create your views here.

def index(request):

    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")
    
def for_doctor(request):
    if request.method == "POST":
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        profilepicture = request.POST.get('profilepicture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact(Firstname=Firstname, Lastname=Lastname, profilepicture=profilepicture,username = username,email = email,address = address,address2 = address2, city=city,state=state,zip=zip)
        contact.save()
    return render(request, "for_doctor.html")
    

def for_patient(request):
    if request.method == "POST":
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        profilepicture = request.POST.get('profilepicture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact_1(Firstname=Firstname, Lastname=Lastname, profilepicture=profilepicture,username = username,email = email,address = address,address2 = address2, city = city,state=state,zip=zip)
        contact.save()
    return render(request, "for_patient.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")
    