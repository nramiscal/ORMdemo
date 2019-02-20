from django.shortcuts import render, HttpResponse, redirect
from .models import Student

def index(request):
    # Student.objects.create(fname="Bella", lname="Ramiscal")

    students = Student.objects.all()
    print(students)

    # myname = "Bella"
    # request.session['email'] = "bella@gmail.com"
    # request.session['test'] = "test@test.com"

    return render(request, "myapp/index.html", {"students": students})

def show(request, number):
    # return HttpResponse("placeholder to display blog number " + str(number))
    return HttpResponse(f"placeholder to display blog number {request.session['test']}")

def process(request):
    # print(request.POST)
    Student.objects.create(fname=request.POST["fname"], lname=request.POST["lname"])
    return redirect("/")
