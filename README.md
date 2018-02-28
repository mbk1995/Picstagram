# Picstagram
### An image gallery.

### Features:
1.	Users can login and create an account to upload images and can also edit the caption or delete their uploaded image
2.	10 images are displayed on the screen in chronological order with the recent at the beginning
3.	The next 10 or previous 10 can be viewed by clicking on the next and previous buttons
4.	Visitors can view all the images uploaded by the users but cannot edit or delete them


### About this Web App:
1.	A Visitor can simply go to http://localhost:8080/ to view all the images uploaded by all the users.
2.	If the visitor wishes to create an account to upload images he can do so by clicking on login and click on register
3.	Now he can upload images by clicking on Add Images in png, jpg or gif format with caption being optional
4.	Once the image is added click on view images to view all the images that he has uploaded and edit the caption or delete the image as required
5.	Steps are edit caption, then add a new caption. Click on ViewImages to navigate back to the gallery with all changes. 
6.	User can logout by clicking on logout button 


### Steps to get started:
1.	Install Python version 3.6.1 from https://www.python.org/downloads/
2.	Install Python Package Manager Pip from https://pip.pypa.io/en/stable/installing/ 
3.	Install Django Framework using the command  `pip install Django==1.9`
4.  Naviagte to the main directory [picstagram]
5.	Sync the SQLite3 database with the project type the command `python manage.py makemigrations`
6.	And then run the command `python manage.py migrate`
7.	To start the server run the command `python manage.py runserver`
8.	Now navigate to http://localhost:8080/ on the web browser for viewing all the images posted by all the users. 
9.	Press Ctrl+C to quit the server
