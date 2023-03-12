## Django Zero to Hero

This is a sample Django project created as a part of the tutorial series "Django Zero to Hero". The purpose of this project is to demonstrate various concepts and features of Django, including models, views, templates, forms, and authentication.

### Getting Started
Prerequisites
Before running this project, you must have the following installed on your system:

- Python 3.x
- Django 4.*
- pip
- virtualenv


## Usage

### Admin Panel
To access the admin panel, go to:

`http://localhost:8000/admin
`
The default username and password are both admin.

Authentication
To register a new user, go to:

`http://localhost:8000/register`

To log in, go to:

`http://localhost:8000/login`

To log out, go to:

`http://localhost:8000/logout`

## Posts
To create a new post, you must be logged in. Go to:

http://localhost:8000/create_post
To view a list of all posts, go to:

http://localhost:8000/posts
To view the details of a specific post, go to:

http://localhost:8000/post/<post_id>
Replace <post_id> with the ID of the post you wish to view.

## Comments

To add a comment to a post, you must be logged in. Go to the details page of the post you wish to comment on and scroll down to the comments section. Enter your comment and click the "Submit" button.