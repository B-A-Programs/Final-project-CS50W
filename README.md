# JobFinder - HarvardX CS50W: Web Programming with Python and JavaScript Final Project
## Technologies used
In creating this app I used [Django](https://www.djangoproject.com/) for the backend (a python framework), while for the frontend I used [Html](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/css/) and [JavaScript](https://www.w3schools.com/js/default.asp), as well as [Bootstrap](https://getbootstrap.com/) to more easily stylise each page.
## Distinctiveness and Complexity
JobFinder is an app which helps companies connect with qualified people looking for jobs in a wide range of fields.  
To achieve this the app uses multiple Django models, has many views each of which can behave differently depending on the request method and/or on any arguments included in the link and the pages use JavaScript to display different elements depending on what the user requests, as well as the device which he is currently using (the app is mobile responsive).
## Files
**Models.py** - contains every model used in my app. A big challange was deciding how to organise this file but in the end I decided that creating more models and then using the relationships between them to acces information would be the best way. Also to distinguish people from companies I used a boolean field and all the information about the user is extracted after checking if it is a company or a person.  
**Views.py** - is the controller of the app. For each page or request it takes in the information and returns a page, possibly changing or adding information in the database if that is what the user requested. For example the   interviews  view first checks that the user is actually a person and then sends to a template all of the users received messages (interviews) from companies, as well as all the job listings where he has applied; before doing this it also checks to see if any interview has passed its due date and if so deletes it.

