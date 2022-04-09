<img width="555" alt="image" src="https://user-images.githubusercontent.com/102805353/162575394-7a887c43-c3f0-4a76-a6ec-d9bb2d91f011.png">

![ezgif com-gif-maker-2](https://user-images.githubusercontent.com/102805353/162577382-e8c60d8a-46ea-4782-8b89-5d4f3d60cb46.gif)


## About

Derived from the levant dialect, Zaaki means delicious, something that all of our recipies are!

At Zaaki we are passionate about sharing the worlds cuisine from the comfort of our kitchen.  Our website assists you with searching for new delicious recipes to explore, We have a vast collection of quick and easy recipies with just an ingredient search away!

Zaaki is a new exciting way of exploring the world through your kitchen! By searching a key ingredient that you have , Zaaki will search for a recipe that holds the key to unlocking your journey around the world! 

Note: -----

## Systems Architecture

The front-end of the website is user friendly and easily navigate
<img width="662" alt="image" src="https://user-images.githubusercontent.com/102805353/162575104-d4084cbc-0e27-41bc-a048-ca1108f1f4a0.png">


## Backend

Postman was used to test the API for CRUD operations. Please refer to the video for the full explanation and examples.

**FLASK-restful-app:**

The following libraries were added to support the app.route function:
```
import requests
import sqlite3 as sql
import urllib
from random import randint
from flask import Flask, render_template, url_for, request
```
The recipe APP was created by executing the code below:
```
@app.route('/')
@app.route('/home')
def home():
    return render_template("ZKHP.html")
```
Running the app.py file would result in:

<img width="389" alt="image" src="https://user-images.githubusercontent.com/102805353/162568512-5bbfe32e-89a7-47fd-8f2f-0680342126d4.png">

**Cloud App:**

<img width="350" alt="image" src="https://user-images.githubusercontent.com/102805353/162575286-f529117f-80b0-49ce-a309-be1942d79da5.png">



This application is served over the Heroku cloud platform.

The application is not currently load balanced but supports HTTPS for the deployment of the app.

To run the app on your local machine you can use the command:
```
  $ flask run --cert=adhoc
```

## Front End

The current version of the front-end can only be ran locally. It was successfully tested on macOS Big Sur launched over the command line. The IOS simulator or Android emulator can be launched through the web interface of the local server. Node.js is required alongside with the respective Node version, please see nvm and docker section above in further detail.
![ezgif com-gif-maker-3](https://user-images.githubusercontent.com/102805353/162577654-b6864fa6-d16f-4b88-b195-c6d608248caf.gif)

