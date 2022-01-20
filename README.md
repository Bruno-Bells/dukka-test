# Receipts Generation/ power test 

![GitHub repo size](https://img.shields.io/github/repo-size/bruno-odinukweze/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/bruno-odinukweze/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/bruno-odinukweze/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/bruno-odinukweze/README-template.md?style=social)
<!-- ![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

Receipts Generation is a project that enable users to generate upto 10 receipts for a given transaction in a click. 

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have python 3.6 + installed on your OS

## Installing Receipt Generation

To install Receipt Generation, follow these steps:

Clone the Project:
```
git clone https://github.com/Bruno-Odinukweze/dukka-test.git
```
```
cd dukka-test
```

create and activate virtual environment and:

```
pip install -r requirements.txt
```

## Using Receipt Generation

To Run the project localy, you will need to make some changes to the API urls in the template (this is if you want to use the HTML/JS User Interface):

locate the template file:
```
dukka-test > core > templates > core > pdf_gen.html
```
change the url network location or domain from `dukka-test.herokuapp.com` to `localhost:800` and save the chages




Make migrations:
```
python manage.py makemigrations
```
Migrate the database:
```
python manage.py migrate
```
run development server:
```
python manage.py runserver
```

open in the browser:
```
http://localhost:8000
```

However, to save yourself the hassle of setting up locally; see the project live: http://dukka-test.herokuapp.com/

## Contact

If you want to contact me you can reach me at brunoodinukweeze1@gmail.com.

## License

This project uses the following license: [<MIT license>](<https://github.com/Bruno-Odinukweze/dukka-test/blob/main/LICENSE>).

