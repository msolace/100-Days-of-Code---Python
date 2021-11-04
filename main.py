import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 44.977753 # Your latitude
MY_LONG = -93.265015 # Your longitude
MY_EMAIL = "matfakeaccount@yahoo.com"
MY_PASSWORD = "jkjtocdnqsiacfmz"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + 5) > iss_latitude > (MY_LAT - 5) and (MY_LONG + 5) > iss_longitude > (MY_LONG - 5):
        print("Its close!")
        return True
    else:
        print(f"Nope, my lat and long: {MY_LAT}, {MY_LONG}. ISS lat and long: {iss_latitude}, {iss_longitude}")
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = 7
    sunset = 19

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    # If the ISS is close to my current position and it is night
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="mathew.solace@gmail.com",
                msg="Subject:LOOK UP AT ISS!\n\nThe ISS is above you, look up!!"
            )











