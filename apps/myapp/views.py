from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    # Student.objects.create(fname="Bella", lname="Ramiscal")

    students = Student.objects.all()
    # print(students)

    # myname = "Bella"
    # request.session['email'] = "bella@gmail.com"
    # request.session['test'] = "test@test.com"

    return render(request, "myapp/index.html", {"students": students})

def show(request, number):
    # return HttpResponse("placeholder to display blog number " + str(number))
    return HttpResponse(f"placeholder to display blog number {request.session['test']}")

def process(request):
    # run the custom validator method we created in StudentManager (in models.py)
    errors = Student.objects.registerValidator(request.POST)
    print(errors)

    # if there are errors, copy our error messages into Django "messages" (like flash in Flask) and redirect to the form so user can resubmit information
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        # passed validation, so create student record and redirect to success
        Student.objects.create(fname=request.POST["fname"], lname=request.POST["lname"])
        return redirect("/success")

def success(request):
    return render(request, "myapp/success.html")
