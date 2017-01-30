student-companion-backend
=======================================
This repository contains work on our backend Django REST Framework application.

Setup
-----

Software
  - `Python 3.5 <https://python.org/>`_
  
.. code-block:: bash

  # Change directory to the project folder
  cd student-companion-backend

  # Create virtual environment
  python3 -m venv venv
  
  # Activate virtual environment
  source venv/bin/activate
  
  # Install requirements
  pip install -r requirements/base.txt
  
  # Add configuration file to your path (add it to your .bashrc or
  # will have to repeat it every time before using manage.py)
  export DJANGO_SETTINGS_MODULE=configuration.settings.local
  
  # Migrate database
  student_companion/manage.py migrate
  
  # Create super user
  student_companion/manage.py createsuperuser
 
  

Usage
-----
Use ``manage.py runserver`` command to start the server.

Go to ``http://localhost:8000/admin`` url to open the administration site.
