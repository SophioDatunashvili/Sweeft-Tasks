To RUN The Project:

*Download the project

*Open project in your IDE.

*Add virtual environment and activate it with following commands:
python3 -m venv venv
source venv/bin/activate

*run the following:
pip install requirements.txt
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver
