# Simple Django Food Portal 
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


Screenshots:

Home Page:


![homepage](https://user-images.githubusercontent.com/51675975/122640588-ff27fe80-d11d-11eb-89ab-dbc7b88af1c6.png)


![homepage-1](https://user-images.githubusercontent.com/51675975/122640587-fd5e3b00-d11d-11eb-8be1-7b282b48ea74.png)


Search By Location:

![Searchbylocation-result](https://user-images.githubusercontent.com/51675975/122640607-2088ea80-d11e-11eb-9649-c05ff16c23d3.png)


![Searchbylocation](https://user-images.githubusercontent.com/51675975/122640610-21ba1780-d11e-11eb-99ee-878fa052c3c6.png)


Upload Datas:

![uploadsucess](https://user-images.githubusercontent.com/51675975/122640626-38f90500-d11e-11eb-8e88-8c6f8b83c550.png)


![upload new content](https://user-images.githubusercontent.com/51675975/122640629-3ac2c880-d11e-11eb-8a53-1fa505299986.png)

