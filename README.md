## Django-bookshop
This application is a simple project created as a project at school.
This is a store with used manuals where logged in users can buy or sell them

### The application includes:
* complete user profile support
* system which check if the given login or e-mail address is used by other user
* email address verification system
* cart system
* fully working payment system (stripe)
* fully working creating sell item views
* and a lot more

## Running the Project Locally

First, clone the repository to your local machine:
```bash
git clone https://github.com/izielin/bookshop.git
```

Move to folder:
```bash
cd bookshop/
```

Create virtual environment and activate it:
```bash
python -m venv venv

on linux:
source venv/bin/activate  

on windows:
source venv/scripts/activate
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Apply the migrations:
```bash
python manage.py migrate
```

Finally, run the development server
```bash
python manage.py runserver
```

Create super user to get access to admin page
```bash
python manage.py createsuperuser
```

The project will be available at **127.0.0.1:8000**.

