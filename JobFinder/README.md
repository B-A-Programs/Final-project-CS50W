# JobFinder - HarvardX CS50W: Web Programming with Python and JavaScript Final Project
## Technologies used
In creating this app I used [Django](https://www.djangoproject.com/) for the backend (a python framework), while for the frontend I used [Html](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/css/) and [JavaScript](https://www.w3schools.com/js/default.asp), as well as [Bootstrap](https://getbootstrap.com/) to more easily stylise each page.
## Distinctiveness and Complexity
JobFinder is an app which helps companies connect with qualified people looking for jobs in a wide range of fields.  
To achieve this the app uses multiple Django models, has many views each of which can behave differently depending on the request method and/or on any arguments included in the link and the pages use JavaScript to display different elements depending on what the user requests, as well as the device which he is currently using (the app is mobile responsive).
## Functionality
#### For all users
- You can see all the registered users and companies.
- You can see all the active job listings. You can also filter them by field and by level (ranging from entry level to advanced).
- You can enter on any job listing's page to see its details
#### For people
- You can edit your description as well as your profile by adding previous job experience, education, courses taken and languages known. You can also delete any previously added qualification from the same edit page.
- You can click apply on any job listing.
- You can see all your applications, as well as any interview you have been called to along with its date, time and location.
#### For companies
- You can create job listings.
- You can invite users to interview or reject them either from the applications page or from the job listing itself.
## Files
**Models.py** - contains every model used in my app. A big challange was deciding how to organise this file but in the end I decided that creating more models and then using the relationships between them to acces information would be the best way. Also to distinguish people from companies I used a boolean field and all the information about the user is extracted after checking if it is a company or a person.  
**Views.py** - is the controller of the app. For each page or request it takes in the information and returns a page, possibly changing or adding information in the database if that is what the user requested. For example the `interviews` view first checks that the user is actually a person and then sends to a template all of the users received messages (interviews) from companies, as well as all the job listings where he has applied; before doing this it also checks to see if any interview has passed its due date and if so deletes it.  
**Admin.py** - renders the admin page from which you (the admin) can control the database.  
**Static** - contains all the static information used on the different pages -> Images, Javascript and CSS.  
**Templates** - contains all the templates used. They display information received from the controller depending on its type and what the specific information is.
## How to use
- Install project dependencies by running `pip install -r requirements.txt`.
- Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
- Create superuser with `python manage.py createsuperuser`. This step is optional, allowing you to manage the database by going on the route `/admin`.
- Go to website address and register an account (either as a user or a company).