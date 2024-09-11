Project Setup Instructions
To set up and run the project, please follow these steps:

Install Required Packages
Run the following command to install all necessary packages listed in req.txt:

python -m pip install -r req.txt

Create Database Migrations
Generate the necessary database migrations with:

python manage.py makemigrations

Apply Database Migrations
Apply the migrations to your database by running:

python manage.py migrate

Start the Development Server
Finally, start the development server using:

python manage.py runserver 0.0.0.0:8000

Quick Copy Command
You can copy and paste the following commands to execute them all at once:

python -m pip install -r req.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 && echo EVERYTHING STARTED 


or write chmod +x /workspace/Weihnachtsbasar_Derksen_Neu_Django_Python/start.cmd and start.cmd

copy: 

chmod +x /workspace/Weihnachtsbasar_Derksen_Neu_Django_Python/start.cmd && start.cmd
