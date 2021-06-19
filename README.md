# django_2_PS
 A simple Django Food Viewing Web Application for restaurants using User Authentcation, Forms, Image Upload and Get Images 

Application Overview:
 This application consist of 2 main applications namely,
  1. Home - which consist of Home Page and Login and Logout logics
  2. Details - which consist of main logics like uploading the contents to the DB and also other logics associated with it.

Running the application:
1. Clone this repository
2. Unzip and from the directory, on the terminal, run 

3. **py manage.py runserver**

4. By default it comes with One Username and password 
   
   Username: admin
   password: admin123

5. Other usernames can be added via admin panal.

URL Endpoints:

 http://127.0.0.1:8000/home/ - Home
 
 http://127.0.0.1:8000/search/<str:city> - Search value based on city name (Can be accessable through **Location Search** Button).
 
 http://127.0.0.1:8000/upload/ - Uploads information (needs User authentication)
 
 http://127.0.0.1:8000/login/ - Login portal
 
 http://127.0.0.1:8000/logout/ - Logout Portal
