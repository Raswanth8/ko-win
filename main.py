import requests
import json
from datetime import date,datetime
import time
import sys

pin = input('Enter Pincode:')
pincode = str(pin)

def appointment_check():

    today = date.today()
    current_date = today.strftime("%d-%m-%Y") #retrieve_today's_date

    now = datetime.now()
    current_time = now.strftime("%I:%M %p") #retrieve_current_time_in_12_hours_format

    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={current_date}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Invalid request")
    
    else:
        data = response.json()
        centers = data["centers"] #get_vaccination_centers

        if len(centers) == 0:
            print(f"No appointment available for next 7 days from {current_date} : Last checking time {current_time}")
        else:
            res ={}
            for center in centers:
                p = center['name'] + f"({center['fee_type']})"
                q = []

                for session in center['sessions']:
                    q.append(str(f"{session['date']} | Age limit :{session['min_age_limit']} | Availability : {session['available_capacity']}"))
                    res[p] = q
            
            p = ' '
            for center,data in res.items():
                p+= ("\n"+center+"\n")
                for dates in data:
                    p += str(dates + "\n")
            
            print(p)
            

            print("Vaccination Dates Available! Exiting now")
            exit()


print("COVID-19 Vaccination Appointment Checker\n")

while(True):
    appointment_check()
    time.sleep(20*30)
        