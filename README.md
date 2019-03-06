# Photo-Opp
This is an online application which allows users search and access an array of photos.
It was generated using Django.

#### Date of Current Version (March 4th,2019)
#### By **Ron Onyonka**

## Description
This is a Django application which allows users to view photos which can be filtered into their different categories and locations.

Try it out : <https://rongallery.herokuapp.com/>
## Prerequisites
You need the following to work on the project: -
* Python version 3.6 
* Pip 
* venv 
* A text Editor(vscode preferably)

## Setup/Installation Requirements
* To start using this project use the following commands:
```bash
$ git clone https://github.com/Ronyonka/photo_opp
```
```bash
$ cd Blog
```

* create a virtual environment
```bash
$ python3.6 -m venv virtual
```
* navigate into the virtual environment
```bash
$ source virtual/bin/activate
```
* while in the Virtual environment install the dependencies found in the  requirements.txt file

```bash
(virtual)$ pip install -r requirements.txt
```
* create a .env file and in it input the following:
```bash
SECRET_KEY=''
DEBUG=True #Set To False in Production
DB_NAME='<Your DB Name>'
DB_USER='<Your DB Username>'
DB_PASSWORD='<Your DB Password>'
DB_HOST='127.0.0.1'
MODE='dev' #set to prod in production
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
```
* add the .env file into the .gitignore
* create a database called gallery
```bash
(virtual)$ psql
ron=# CREATE DATABASE gallery;
```
* make migrations
```bash
(virtual)$ python3.6 manage.py makemigrations photos
(virtual)$ pytohon3.6 manage.py migrate
```

* to run the project enter this command
```bash
(virtual)$ python3.6 manage.py runserver
```
* access the application on this localhost address http://127.0.0.1:8000

## Behaviour Driven Development
| Behaviour     | Input     | Output  |
| ------------- |:-------------:| -----:|
| User wants to see photos | They enter the site | They view a list of uploaded photos |
| User wants to see and enlarged photo | They click on view images | A modal appears with the enlarged image and its details  |
| User wants to search for image | They enter a category name in the search bar | They are directed to a page with images from that category displayed |
| User wants to view images from a certain location | They select a location from a dropdown list | Photos from that location are displayed |

## Link to Live Website 
Here is a link to the live website: <https://rongallery.herokuapp.com/>

## Known Bugs
None known at the moment.

## Technologies Used
* HTML
* JavaScript
* CSS
* Python

## License
MIT License

Copyright (c) 2019 Ron Onyonka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.