import json, datetime
from sqlite3 import Date
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User, Job_experiences, Languages, Education, Courses, Job, Message

def index(request):
    return render(request, "JobFinderApp/index.html")
    
# Returns the profile of a person
def profile(request, username):
    return render(request, "JobFinderApp/profile.html", {
        "person": User.objects.get(username = username)
    })

# Displays a post
def post(request, id):
    return render(request, "JobFinderApp/post.html", {
        "post": Job.objects.get(pk = id)
    })

# Lets the user delete their added qualities or a company delete their posts
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
        elif request.POST["op"] == "post" and Job.objects.get(pk = id).user == request.user:
            Job.objects.get(pk = id).delete()
            return redirect("profile", request.user.username)
        elif request.POST["op"] == "interview" and Message.objects.get(pk = id).person == request.user:
            Message.objects.get(pk = id).job.accepted.remove(Message.objects.get(pk = id).person)
            Message.objects.get(pk = id).delete()
            return redirect("interviews")
        
        return redirect("edit", request.user.username)

# Lets a user add qualities and checks that the data is correct
def edit(request, username):
    if request.method == "GET":
        # Return edit page is user is the same as the request user
        if(request.user.username == username):
            return render(request, "JobFinderApp/edit.html", {
                "person": User.objects.get(username = username)
            })
        else:
            return render(request, 'JobFinderApp/index.html', {
                "message": "You can't acces another user's edit page."
            })
    elif request.method == "POST":
        # Check if request user is the same as the user to be updated
        if request.user.username == username:
            user = User.objects.get(username = username)
            if request.POST["op"] == "desc":
                desc = request.POST["description"]
                user.description = desc
                user.save()
                return redirect("profile", username)
            elif request.POST["op"] == "job":
                company = request.POST["company"]
                position = request.POST["position"]
                description = request.POST["description"]
                start = request.POST["start_date"]
                end = request.POST["end_date"]

                # Check if dates entered are correct
                if start <= str(user.birth_date):
                    return render(request, 'JobFinderApp/edit.html', {
                        "person": User.objects.get(username = username),
                        "message": "Start date must be bigger than your birth date!"
                    })
                
                if start <= end:
                    job = Job_experiences.objects.create(user=user, company_name=company, position=position, description=description, start_date=start, end_date=end)
                    job.save()
                else:
                    return render(request, 'JobFinderApp/edit.html', {
                        "person": User.objects.get(username = username),
                        "message": "Start date must be less than the end date!"
                    })
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

                # Check if dates entered are correct
                if start <= str(user.birth_date):
                    return render(request, 'JobFinderApp/edit.html', {
                        "person": User.objects.get(username = username),
                        "message": "Start date must be bigger than your birth date!"
                    })

                if(start <= end):
                    educ = Education.objects.create(user=user, institution=institution, level=level, start_date=start, end_date=end)
                    educ.save()
                else:
                    return render(request, 'JobFinderApp/edit.html', {
                        "person": User.objects.get(username = username),
                        "message": "Start date must be less than the end date!"
                    })
            elif request.POST["op"] == "course":
                institution = request.POST["institution"]
                name = request.POST["name"]
                c = Courses.objects.create(user=user, institution=institution, name=name)
                c.save()
            elif request.POST["op"] == "field":
                user.field = request.POST.get("fieldofinterest", False)
                if user.field != False:
                    user.save()
                else:
                    # Check if there is a correct field selected
                    return render(request, 'JobFinderApp/edit.html', {
                        "person": User.objects.get(username = username),
                        "message": "You must select a field when changing it!"
                    })
            return redirect("edit", user.username)
        else:
            return redirect("index")

# Lets a company create a post
def create_post(request):
    if request.method == "GET":
        return render(request, "JobFinderApp/create_post.html")
    elif request.method == "POST":
        if request.user.is_company:
            title = request.POST["title"]
            level = request.POST.get("level", False)

            # Check if there is a correct level selected
            if level == False:
                return render(request, "JobFinderApp/create_post.html", {
                    "message": "You must select a level for your job post!"
                })

            # Add color attribute based on level
            if level == "Entry level":
                color = "green"
            elif level == "Beginner":
                color = "orange"
            elif level == "Intermediate":
                color = "magenta"
            else:
                color = "red"

            description = request.POST["description"]
            requirements = request.POST["requirements"]
            compensation = request.POST["compensation"]
            field = request.POST.get("fieldofinterest", False)

            # Check if there is a correct field selected
            if field != False:
                post = Job.objects.create(user=request.user, title=title, level=level, description=description, requirements=requirements, compensation=compensation, field=field, color=color)
                post.save()
            else:
                return render(request, "JobFinderApp/create_post.html", {
                    "message": "You must select a field for your job post!"
                })
        return redirect("profile", request.user.username)

# Lets a user apply and unapply to a post
def apply(request, id):
    if request.method == "POST":
        job = Job.objects.get(pk = id)
        if request.user in job.applicants.all():
            job.applicants.remove(request.user)
        else:
            job.applicants.add(request.user)

        return redirect("post", job.id)

# Lets a company delete a users application
def reject(request, id):
    if request.method == "POST":
        job = Job.objects.get(pk = request.POST["jobid"])
        user = User.objects.get(pk = id)

        if request.user == job.user:
            job.applicants.remove(user)
            job.accepted.remove(user)
            return redirect("applicants")

# Lets a company view all active applications to their job listings
def applicants(request):
    if request.user.is_company:
        app = Message.objects.filter(company = request.user)

        # Delete any interview overdue, else append user to accepted applicants
        for a in app:
            if a.date < datetime.date.today():
                a.job.accepted.remove(a.person)
                a.delete()
        return render(request, "JobFinderApp/applicants.html", {
            "posts": Job.objects.filter(user = request.user)
        })

# Lets a company schedule a meeting
def message(request):
    if request.method == "POST":
        job = Job.objects.get(pk = request.POST["job"])
        company = job.user
        if request.user == company:
            applicant = User.objects.get(pk = request.POST["applicant"])
            date = request.POST["date"]
            time = request.POST["time"]
            location = request.POST["location"]

            # Check if time is in correct format
            if len(time) != 5 or time[2] != ":" or time[1] not in "0123456789" or time[0] not in "012" or time[3] not in "012345" or time[4] not in "0123456789":
                return render(request, "JobFinderApp/applicants.html", {
                    "posts": Job.objects.filter(user = request.user),
                    "message": "Time must be in format hh:mm!"
                })

            mes = Message.objects.create(person=applicant, job=job, company=company, date=date, time=time, location=location)
            mes.save()
            job.accepted.add(applicant)

            return redirect("applicants")

# Page for displaying a user's pending interviews
def interviews(request):
    if not request.user.is_company:
        interviews = Message.objects.filter(person=request.user)
        # Delete any interviews overdue
        for interview in interviews:
            if interview.date < datetime.date.today():
                interview.job.accepted.remove(interview.person)
                interview.delete()
        return render(request, "JobFinderApp/interviews.html", {
            'interviews': Message.objects.filter(person=request.user),
            'job_applications': Job.objects.filter(applicants=request.user)
        })

# Page for displaying posts
def posts(request, field, level):
    if field != "all" and level != "any":
        return render(request, "JobFinderApp/posts.html", {
            'title': f"Job posts in the field of: {field} | Level: {level}",
            'posts': Job.objects.filter(field = field, level = level),
            'field': field,
            'level': level
        })
    elif field != "all":
        return render(request, "JobFinderApp/posts.html", {
            'title': f"Job posts in the field of: {field}",
            'posts': Job.objects.filter(field = field),
            'field': field
        })
    else:
        return render(request, "JobFinderApp/posts.html", {
            'title': "All posts",
            'posts': Job.objects.all()
        })

# Page for displaying users
def users(request, field):
    if field != "all":
        return render(request, "JobFinderApp/users.html", {
            'title': field,
            'people': User.objects.filter(field = field, is_company = False),
            'companies': User.objects.filter(field = field, is_company = True)
        })
    else:
        return render(request, "JobFinderApp/users.html", {
            'title': field,
            'people': User.objects.filter(is_company = False),
            'companies': User.objects.filter(is_company = True)
        })


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

def register_company(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        location = request.POST["location"]
        location_link = request.POST["location_link"]
        field = request.POST.get("field", False)

        # Check if field is correct
        if field == False:
            return render(request, "JobFinderApp/register_company.html", {
                "message": "Main field of operations must not be empty!"
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "JobFinderApp/register_company.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new company type user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, is_company=True, location=location, link_to_location=location_link, field=field)
            user.save()
        except IntegrityError:
            return render(request, "JobFinderApp/register_company.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "JobFinderApp/register_company.html")