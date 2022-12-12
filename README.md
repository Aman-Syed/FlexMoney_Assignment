# FlexMoney_Assignment
Developed a website for registering to yoga classes and viewing their membership. 
Django Framework is used for developing the website . 
A TOUR AROUND THE WEBSITE :
->The website starts with a login and registration pages . People already having an account can login and new users can register .
<img width="1440" alt="Screenshot 2022-12-12 at 10 23 24 PM" src="https://user-images.githubusercontent.com/83821477/207105492-87e377a7-c1b4-4745-9e1f-de47674e052d.png">
<img width="1440" alt="Screenshot 2022-12-12 at 10 25 17 PM" src="https://user-images.githubusercontent.com/83821477/207106032-1cf4e073-322f-4afb-8aaa-6ace9581e7e1.png">
->New User has to satisfy the given constrains
    1.Age above 18 and below 65 . If not it prompts for entering valid age 
    <img width="1440" alt="Screenshot 2022-12-12 at 10 27 51 PM" src="https://user-images.githubusercontent.com/83821477/207106544-44b05b50-0e6a-4575-bd31-6b1af4081f66.png">
    2.Phone number should be valid . If not it prompts for entering valid number
    <img width="1440" alt="Screenshot 2022-12-12 at 10 28 26 PM" src="https://user-images.githubusercontent.com/83821477/207106720-0cb368b1-77fe-4076-974a-bd1054616d7e.png">
    3.Upon Successful registration . The webpage displays registration details and amount paid.
    <img width="1440" alt="Screenshot 2022-12-12 at 10 30 13 PM" src="https://user-images.githubusercontent.com/83821477/207107051-35a933bb-150d-41af-8eef-1d05bd147423.png">
    <img width="1440" alt="Screenshot 2022-12-12 at 10 31 05 PM" src="https://user-images.githubusercontent.com/83821477/207107257-17bce41c-8033-465d-94c5-192b1e6718d8.png">

    4.If a user already exists with that mail . It prompts an httpresponse to login.
    <img width="1440" alt="Screenshot 2022-12-12 at 10 31 22 PM" src="https://user-images.githubusercontent.com/83821477/207107322-b9ed20d6-67b0-45d1-b741-6a5f2d1cb37a.png">
    5. For an existing user, upon successful login , gets details of his/her membership.
    <img width="1440" alt="Screenshot 2022-12-12 at 10 33 16 PM" src="https://user-images.githubusercontent.com/83821477/207107755-e25fbd8b-d5ed-43aa-a822-c8c5ef9c99a0.png">

    <img width="1440" alt="Screenshot 2022-12-12 at 10 32 38 PM" src="https://user-images.githubusercontent.com/83821477/207107608-059a83de-c7de-4d07-88e3-0e502b5c8619.png">
    6.If the membership of the person has expired/ the person didnt take membership for that particular month upon loggin it asks for payment to continue.
    <img width="1440" alt="Screenshot 2022-12-12 at 10 34 45 PM" src="https://user-images.githubusercontent.com/83821477/207108048-38ce6611-8356-4e54-a3f9-7cf1e8594043.png">
    7.If login attempt is unsuccessful it prompts an HttpResponse.
    <img width="1440" alt="Screenshot 2022-12-12 at 10 35 40 PM" src="https://user-images.githubusercontent.com/83821477/207108248-eacd9c94-a637-452c-bb8e-2133112f28a0.png">

KEYPOINTS OF THE CODE:
->INSIDE THE YOGA APP PROJECT DEVELOPMENT IS DONE.
->DATABASE USED HERE IS Sqlite3 (built in SQL Database used by Django).
->Yoga app consists of 
1.models.py - It consists of all the tables (User and Reservations) and the fields along with specifications.
2.views.py- It consists of the backend logic and database operations are done .
->TEMPLATE FOLDER CONSISTS OF THE HTML FILES.

ER DIAGRAM :
 Entity Relationship Diagram depicts relationship between entity sets . They provide a visual starting point for database design.
 ![Blank diagram](https://user-images.githubusercontent.com/83821477/207111231-9c5c6d9d-df80-40b9-b554-0d211f34d736.jpeg)

DATABASE:

TABLES 
1. USER TABLE 
   Attributes - name,email,password,phone number,age,user id.
2. RESERVATION TABLE
   Attributes - reservation id , user id, payment amount,batch,month,year
   
