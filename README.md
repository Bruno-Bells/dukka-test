# Receipts Generation/ power test 

![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)
<!-- ![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

Receipts Generation is a project that enable users to generate upto 10 receipts for a given transaction in a click. 

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed all the dependencies in the requirements.txt

## Installing Receipt Generation

To install Receipt Generation, follow these steps:

Clone the Project:
```
git clone https://github.com/Bruno-Odinukweze/dukka-test.git
```

create virtual environment and install dependencies
```
cd dukka-test
```
```
pip install -r requirements.txt
```

## Using Receipt Generation

To Run the project localy, you will need to make some changes to the API urls in the template:

locate the template file:
```
dukka-test > core > templates > core > pdf_gen.html
```
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

However, to save yourself the hassle of setting up locally; see the project live: http://dukka-test.herokuapp.com/

## Contact

If you want to contact me you can reach me at <your_email@address.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [<license_name>](<link>).

