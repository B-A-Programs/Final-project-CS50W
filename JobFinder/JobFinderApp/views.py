import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User, Job_experiences, Languages, Education, Courses

def index(request):
    return render(request, "JobFinderApp/index.html")
    
def profile(request, username):
    return render(request, "JobFinderApp/profile.html", {
        "person": User.objects.get(username = username)
    })

def delete(request, id):
    if request.method == "POST":
        if request.POST["op"] == "job" and Job_experiences.objects.get(pk = id).user == request.user:
            Job_experiences.objects.get(pk = id).delete()
        elif request.POST["op"] == "educ" and Education.objects.get(pk = id).user == request.user:
            Education.objects.get(pk = id).delete()
        elif request.POST["op"] == "lang" and Languages.objects.get(pk = id).user == request.user:
            Languages.objects.get(pk = id).delete()
        elif request.POST["op"] == "course" and Courses.objects.get(pk = id).user == request.user:
            Courses.objects.get(pk = id).delete()
        
        return redirect("profile", request.user.username)

def edit(request, username):
    if request.method == "GET":
        if(request.user.username == username):
            return render(request, "JobFinderApp/edit.html", {
                "person": User.objects.get(username = username)
            })
        else:
            return redirect('index')
    elif request.method == "POST":
        if request.user.username == username:
            user = User.objects.get(username = username)
            if request.POST["op"] == "desc":
                desc = request.POST["description"]
                user.description = desc
                user.save()
            elif request.POST["op"] == "job":
                company = request.POST["company"]
                position = request.POST["position"]
                description = request.POST["description"]
                start = request.POST["start_date"]
                end = request.POST["end_date"]
                if(start <= end):
                    job = Job_experiences.objects.create(user=user, company_name=company, position=position, description=description, start_date=start, end_date=end)
                    job.save()
            elif request.POST["op"] == "lang":
                language = request.POST["language"]
                level = request.POST["level"]
                lang = Languages.objects.create(user=user, language=language, level=level)
                lang.save()
            elif request.POST["op"] == "educ":
                institution = request.POST["institution"]
                level = request.POST["level"]
                start = request.POST["start_date"]
                end = request.POST["end_date"]
                if(start <= end):
                    educ = Education.objects.create(user=user, institution=institution, level=level, start_date=start, end_date=end)
                    educ.save()
            elif request.POST["op"] == "course":
                institution = request.POST["institution"]
                name = request.POST["name"]
                c = Courses.objects.create(user=user, institution=institution, name=name)
                c.save()
            return redirect("edit", user.username)
        else:
            return redirect("index")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "JobFinderApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "JobFinderApp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        date = request.POST["date"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "JobFinderApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, last_name=last, first_name=first, birth_date=date)
            user.save()
        except IntegrityError:
            return render(request, "JobFinderApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "JobFinderApp/register.html")
