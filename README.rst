student-companion-backend
=======================================
This repository contains work on our backend Django REST Framework application.

Setup
-----

Software
  - `Python 3.5 <https://python.org/>`_ (If you use Windows make sure to select option to add Python to PATH)
  
.. code-block:: bash

  # Change directory to the project folder
  cd student-companion-backend

  # Create virtual environment
  python -m venv venv
  
  # Activate virtual environment (Linux)
  source venv/bin/activate
  
  # Activate virtual environment (Windows Power Shell)
  venv/Scripts/Activate.ps1
  
  # Install requirementst
  pip install -r requirements/base.txt
  
  # Add configuration file to your path (add it to your .bashrc or
  # will have to repeat it every time before using manage.py)
  export DJANGO_SETTINGS_MODULE=configuration.settings.local
  
  # On Windows
  set DJANGO_SETTINGS_MODULE=configuration.settings.local
  
  # Go to the folder that has the management script in (manage.py)
  cd student_companion
  
  # Migrate database
  python manage.py migrate
  
  # Create super user
  python manage.py createsuperuser
 
  

Usage
-----
Make sure to activate virtual environment (``source venv/bin/activate`` on Linux or ``venv/Scripts/Activate.ps1`` on Windows' Power Shell) everytime you execute the following commands. It needs to show (venv) by the left side of every line in the terminal.

Use ``python manage.py runserver`` command to start the server.

Go to ``http://localhost:8000/admin`` url to open the administration site.
