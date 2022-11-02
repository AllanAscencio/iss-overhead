ISS Over Head

This project was built to know when the International Spaceship Station is within a range of +5 or -5 of my current location using the ISS API and emailing this notification to myself to know instantly when this happens.

This project made me work on my skills with API requests and getting to know the functionality of it.

The project is written in python using python 3.11 as the interpreter and also using four different libraries:
- requests
- datetime
- smtplib
- time

How to Use

In order to use this program properly I suggest you go into https://www.google.cl/maps and find your location, latitude and longitude. 

Once you have that, you can open main.py on your IDE (I used PyCharm and VSCode) and change the variables called "MY_LAT" and "MY_LONG". Another way is to head to https://www.latlong.net/ and write the name of your city and it will give the latitude and longitude as well.

Then you need to change the variable "my_email" with your own email and keep in mind I was working with a gmail test account, therefor you will need to enable the app password on gmail to get this going.

After you have that done you are ready to go.
