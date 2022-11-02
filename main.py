import requests
from datetime import datetime
import smtplib
import time

my_email = "testallan01@gmail.com"
pw = "lcgugrsfkkmynpgb"


MY_LAT = -41.4717
MY_LONG = -72.9396


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = str(float(data["iss_position"]["latitude"]))
    iss_longitude = str(float(data["iss_position"]["longitude"]))
    if -46.4717 >= float(iss_latitude) >= -36.4717 and -77.9396 >= float(iss_longitude) >= -67.9396:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Look up!\n\nThe ISS is above you in the sky"
            )



