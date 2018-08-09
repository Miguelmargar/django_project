# Luca D'Ettore
**Ecommerce Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's classroom bootcamp. It is a **fictional** Ecommerce site built with Python's *Django* framework - no template was used.

## Live Demo

**Follow this link to view deployed version of the web app https://miguel-django-project.herokuapp.com/**

## Tech Used

### Some the tech used includes:
- **HTML**, **CSS** and **Javascript**
  - Base languages used to create website
- [Django](https://www.djangoproject.com/)
    - We use **Django** to handle page routing and to build custom directives
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [Hover.css](http://ianlunn.github.io/Hover/)
    - use hover.css to obtain the underline in the navbar links
- [Google Fonts](https://fonts.google.com/)
    - use of google font "Luckiest Guy"
- [Font Awsome](https://fontawesome.com/)
    - Font Awsome has been used for the icons in all the pages

## URL's

urls.py at the project level (topcommerce) gives the url patterns routes to views for the Apps that have their own urls, via the 'include' function:

 `from accounts import urls as accounts_urls`

 `urlpatterns = [path('accounts/', include(accounts_urls))]`

## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block content %}
{% endblock content %}
```
Which allows other templates to be inserted in to that section (within the <main> section). Linking the base.html to templates within Apps:
```
{% extends 'base.html' %}

{% block content %}

```
All code for the app goes in here & will appear between the navbar & footer from base.html
```
{% endblock content %}
```

## Apps

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in users can view their own profile that will display their username and email address they used to register with. Users can also visualise their shortlist of items(cart) and the option to log out once loged in. Seller registration functionality is included however it is not showing or used as the purpose of the website is for a manufacturer of watches to sell their own watches. Therefore the buyer model is the only one used. 

#### Products

This App displays the Products that have been added via Django's admin panel. This App has the ability to search products with a simple Python function to search through all the products & render the products.html page which displays them.

#### Shortlist

The Cart App stores the quantity and price of all products selected and disaplays a basket total. 

#### checkout

The checkout App renders the products of the shortlist App and a form for a one-off Stripe payment. Once paid there is a html confirmation and a text confirmation sent to the user.

## Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended to base.py and local.py was created to handle the local resources while prod.py was created for the database & static files to point to the online resources.

## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

`$ python3 manage.py test <app name>`

* `$ python3 manage.py test accounts` - These will all PASS
    tests_forms.py in the Accounts App:
    1. Tests that the login form is valid with the correct detials
    2. Tests that the UserRegistrationForm validates properly when the correct information is supplied
    3. Tests that the registration form fails when one of the passwords has not been entered
    4. Tests that the registration form fails when the passwords do not match
    tests_models.py in the Accounts App:
    1. Tests that the buyer and seller model is correct

* `$ python3 manage.py test products` - This will PASS
    tests.py in the Products App:
    1. Tests that the product name label is functioning correctly

* `$ python3 manage.py test shortlist` - These will PASS
    tests.py in the Shortlist App:
    1. Tests that the url for '/shortlist/' resolves to the correct viewshortlist.html

## Special Thanks

Not in any specific order

1. To Luca D'Ettore for allowing me to use his name for this fictional website
2. Richard Dalton for his time teaching and help when needed
3. Katie Maxwell for her help when needed during the course
4. Code Institute in general for arranging and developing the course




