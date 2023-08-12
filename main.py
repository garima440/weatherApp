from tkinter import *
# import tkinter as tk
from PIL.ImageTk import PhotoImage
from tkmacosx import Button
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

window = Tk()
window.title("Weather App")
window.geometry("890x470+300+300")
window.configure(bg="#BAD7E9")
window.resizable(False, False)


def get_weather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)

    if location.latitude >= 0 and location.longitude >= 0:
        long_lat.config(text=f"{abs(round(location.latitude, 1))}° N, {abs(round(location.longitude, 1))}° E")

    if location.latitude < 0 and location.longitude < 0:
        long_lat.config(text=f"{abs(round(location.latitude, 1))}° S, {abs(round(location.longitude, 1))}° W")

    if location.latitude > 0 > location.longitude:
        long_lat.config(text=f"{abs(round(location.latitude, 1))}° N, {abs(round(location.longitude, 1))}° W")

    if location.latitude < 0 < location.longitude:
        long_lat.config(text=f"{abs(round(location.latitude, 1))}° S, {abs(round(location.longitude, 1))}° E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    current_date = local_time.strftime("%d %B, %Y")
    clock.config(text=current_time)
    date.config(text=current_date)

    api1 = f"https://api.openweathermap.org/data/3.0/onecall?lat={location.latitude}&lon={location.longitude}&exclude" \
           f"=hourly&appid=3f7d80fb664bb99e24035fc4b9472e8b&units=metric"

    air_quality_api = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={location.latitude}&" \
                      f"lon={location.longitude}&appid=3360b47f29c2bca35ca47dcfd9d74810"

    json_data = requests.get(api1).json()
    air_quality_data = requests.get(air_quality_api).json()

    air_quality = air_quality_data['list'][0]['main']['aqi']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    if air_quality == 1:
        air_quality_label.config(text=f"{air_quality} (Good)")
    if air_quality == 2:
        air_quality_label.config(text=f"{air_quality} (Fair)")
    if air_quality == 3:
        air_quality_label.config(text=f"{air_quality} (Moderate)")
    if air_quality == 4:
        air_quality_label.config(text=f"{air_quality} (Poor)")
    if air_quality == 5:
        air_quality_label.config(text=f"{air_quality} (Very Poor)")

    humidity_label.config(text=f"{humidity}%")
    pressure_label.config(text=f"{pressure} hPa")
    wind_label.config(text=f"{wind} m/s")
    description_label.config(text=f"{description}")

    # days
    first_day = datetime.now(home)
    day1.config(text=first_day.strftime("%A"))

    second_day = first_day + timedelta(days=1)
    day2.config(text=second_day.strftime("%a"))

    third_day = second_day + timedelta(days=1)
    day3.config(text=third_day.strftime("%a"))

    fourth_day = third_day + timedelta(days=1)
    day4.config(text=fourth_day.strftime("%a"))

    fifth_day = fourth_day + timedelta(days=1)
    day5.config(text=fifth_day.strftime("%a"))

    sixth_day = fifth_day + timedelta(days=1)
    day6.config(text=sixth_day.strftime("%a"))

    seventh_day = sixth_day + timedelta(days=1)
    day7.config(text=seventh_day.strftime("%a"))

    # first cell image and day night temperature
    icon1 = json_data['current']['weather'][0]['icon']
    opened_image1 = (Image.open(f"icons/{icon1}.png"))
    resized_img1 = opened_image1.resize((52, 52))
    first_image = ImageTk.PhotoImage(resized_img1)
    image1.config(image=first_image)
    image1.image = first_image

    day1_temp = json_data['current']['temp']
    temp_label1.config(text=f"{round(day1_temp, 1)}°C")

    day1_feels_like = json_data['current']['feels_like']
    feels_like_label1.config(text=f"Feels like: {round(day1_feels_like, 1)}°C")

    # second cell image and day night temperature
    icon2 = json_data['daily'][0]['weather'][0]['icon']
    opened_image2 = (Image.open(f"icons/{icon2}.png"))
    resized_img2 = opened_image2.resize((30, 30))
    second_image = ImageTk.PhotoImage(resized_img2)
    image2.config(image=second_image)
    image2.image = second_image

    daytime_temp2 = json_data['daily'][0]['temp']['day']
    nighttime_temp2 = json_data['daily'][0]['temp']['night']
    day_night_temp_label2.config(text=f"Day: {daytime_temp2}\n Night: {nighttime_temp2}")

    # third cell image and day night temperature
    icon3 = json_data['daily'][1]['weather'][0]['icon']
    opened_image3 = (Image.open(f"icons/{icon3}.png"))
    resized_img3 = opened_image3.resize((30, 30))
    third_image = ImageTk.PhotoImage(resized_img3)
    image3.config(image=third_image)
    image3.image = third_image

    daytime_temp3 = json_data['daily'][1]['temp']['day']
    nighttime_temp3 = json_data['daily'][1]['temp']['night']
    day_night_temp_label3.config(text=f"Day: {daytime_temp3}\n Night: {nighttime_temp3}")

    # fourth cell image and day night temperature
    icon4 = json_data['daily'][2]['weather'][0]['icon']
    opened_image4 = (Image.open(f"icons/{icon4}.png"))
    resized_img4 = opened_image4.resize((30, 30))
    fourth_image = ImageTk.PhotoImage(resized_img4)
    image4.config(image=fourth_image)
    image4.image = fourth_image

    daytime_temp4 = json_data['daily'][2]['temp']['day']
    nighttime_temp4 = json_data['daily'][2]['temp']['night']
    day_night_temp_label4.config(text=f"Day: {daytime_temp4}\n Night: {nighttime_temp4}")

    # fifth cell image and day night temperature
    icon5 = json_data['daily'][3]['weather'][0]['icon']
    opened_image5 = (Image.open(f"icons/{icon5}.png"))
    resized_img5 = opened_image5.resize((30, 30))
    fifth_image = ImageTk.PhotoImage(resized_img5)
    image5.config(image=fifth_image)
    image5.image = fifth_image

    daytime_temp5 = json_data['daily'][3]['temp']['day']
    nighttime_temp5 = json_data['daily'][3]['temp']['night']
    day_night_temp_label5.config(text=f"Day: {daytime_temp5}\n Night: {nighttime_temp5}")

    # sixth cell image and day night temperature
    icon6 = json_data['daily'][4]['weather'][0]['icon']
    opened_image6 = (Image.open(f"icons/{icon6}.png"))
    resized_img6 = opened_image6.resize((30, 30))
    sixth_image = ImageTk.PhotoImage(resized_img6)
    image6.config(image=sixth_image)
    image6.image = sixth_image

    daytime_temp6 = json_data['daily'][4]['temp']['day']
    nighttime_temp6 = json_data['daily'][4]['temp']['night']
    day_night_temp_label6.config(text=f"Day: {daytime_temp6}\n Night: {nighttime_temp6}")

    # seventh cell image and day night temperature
    icon7 = json_data['daily'][5]['weather'][0]['icon']
    opened_image7 = (Image.open(f"icons/{icon7}.png"))
    resized_img7 = opened_image7.resize((30, 30))
    seventh_image = ImageTk.PhotoImage(resized_img7)
    image7.config(image=seventh_image)
    image7.image = seventh_image

    daytime_temp7 = json_data['daily'][5]['temp']['day']
    nighttime_temp7 = json_data['daily'][5]['temp']['night']
    day_night_temp_label7.config(text=f"Day: {daytime_temp7}\n Night: {nighttime_temp7}")


# labels
label1 = Label(window,
               text="Air Quality",
               font=("Helvetica", 14),
               fg="#2B3467",
               bg="#BAD7E9")
label1.place(x=50, y=120)

label2 = Label(window,
               text="Humidity",
               font=("Helvetica", 14),
               fg="#2B3467",
               bg="#BAD7E9")
label2.place(x=50, y=140)

label3 = Label(window,
               text="Pressure",
               font=("Helvetica", 14),
               fg="#2B3467",
               bg="#BAD7E9")
label3.place(x=50, y=160)

label4 = Label(window,
               text="Wind speed",
               font=("Helvetica", 14),
               fg="#2B3467",
               bg="#BAD7E9")
label4.place(x=50, y=180)

label5 = Label(window,
               text="Description",
               font=("Helvetica", 14),
               fg="#2B3467",
               bg="#BAD7E9")
label5.place(x=50, y=200)

# search box

search_bar = PhotoImage(file="images/search_bar_for_weatherApp.drawio.png")
search_label = Label(image=search_bar, bg="#BAD7E9")
search_label.place(x=300, y=120)

weather_image = PhotoImage(file="images/search-bar-icon.png")
weather_label = Label(window, image=weather_image, bg="#2B3467")
weather_label.place(x=318, y=125)

textfield = Entry(window,
                  justify="center",
                  width=13,
                  font=('poppins', 22, 'normal'),
                  bg="#2B3467",
                  highlightthickness=0,
                  insertbackground='white',
                  border=0,
                  fg='white')
textfield.focus_set()
textfield.place(x=353, y=129)

search_icon = PhotoImage(file="images/search_icon.png")
search_icon_button = Button(window,
                            image=search_icon,
                            cursor='hand2',
                            borderwidth=0,
                            bg="#2B3467",
                            bd=0,
                            width=30,
                            bordercolor="#2B3467",
                            command=get_weather)
search_icon_button.place(x=551, y=126)

# bottom-boxes

frame = Frame(window, width=900, height=180, bg="#2B3467")
frame.pack(side=BOTTOM)

first_box = PhotoImage(file="images/box1.drawio (1).png")
second_box = PhotoImage(file="images/box2.drawio.png")

Label(frame, image=first_box, bg="#2B3467").place(x=50, y=35)
Label(frame, image=second_box, bg="#2B3467").place(x=275, y=40)
Label(frame, image=second_box, bg="#2B3467").place(x=375, y=40)
Label(frame, image=second_box, bg="#2B3467").place(x=475, y=40)
Label(frame, image=second_box, bg="#2B3467").place(x=575, y=40)
Label(frame, image=second_box, bg="#2B3467").place(x=675, y=40)
Label(frame, image=second_box, bg="#2B3467").place(x=775, y=40)

# date
date = Label(window,
             font=("Helvetica", 16),
             fg="#2B3467",
             bg="#BAD7E9")
date.place(x=50, y=20)

# clock
clock = Label(window,
              font=("Helvetica", 30, 'bold'),
              fg="#2B3467",
              bg="#BAD7E9")
clock.place(x=50, y=43)

# timezone
timezone = Label(window, font=('Helvetica', 20),
                 fg="#2B3467",
                 bg="#BAD7E9")
timezone.place(x=680, y=20)

# longitude and latitude
long_lat = Label(window, font=('Helvetica', 16), fg="#2B3467", bg="#BAD7E9")
long_lat.place(x=680, y=47)

# labels for variables
air_quality_label = Label(window,
                          font=('Helvetica', 14),
                          fg="#2B3467",
                          bg="#BAD7E9")
air_quality_label.place(x=150, y=120)

humidity_label = Label(window,
                       font=('Helvetica', 14),
                       fg="#2B3467",
                       bg="#BAD7E9")
humidity_label.place(x=150, y=140)

pressure_label = Label(window,
                       font=('Helvetica', 14),
                       fg="#2B3467",
                       bg="#BAD7E9")
pressure_label.place(x=150, y=160)

wind_label = Label(window,
                   font=('Helvetica', 14),
                   fg="#2B3467",
                   bg="#BAD7E9")
wind_label.place(x=150, y=180)

description_label = Label(window,
                          font=('Helvetica', 14),
                          fg="#2B3467",
                          bg="#BAD7E9")
description_label.place(x=150, y=200)


# frames for bottom cells

# first frame
frame1 = Frame(window, width=161, height=92, bg='#2B3467')
frame1.place(x=58, y=332)

day1 = Label(frame1, font="arial 20", bg="#2B3467", fg="#ffffff")
day1.place(x=65, y=2)

image1 = Label(frame1, bg="#2B3467")
image1.place(x=1, y=16)

temp_label1 = Label(frame1, font="arial 25 bold", bg="#2B3467", fg="#EB455F")
temp_label1.place(x=65, y=30)

feels_like_label1 = Label(frame1, font="arial 12", bg="#2B3467", fg="#EB455F")
feels_like_label1.place(x=60, y=62)

# second frame
frame2 = Frame(window, width=55, height=85, bg='#2B3467')
frame2.place(x=281, y=336)

day2 = Label(frame2, font="arial 14", bg="#2B3467", fg="#ffffff")
day2.place(x=12, y=1)

image2 = Label(frame2, bg="#2B3467")
image2.place(x=11, y=22)

day_night_temp_label2 = Label(frame2, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label2.place(x=-4, y=55)

# third frame
frame3 = Frame(window, width=55, height=85, bg='#2B3467')
frame3.place(x=381, y=336)

day3 = Label(frame3, font="arial 14", bg="#2B3467", fg="#ffffff")
day3.place(x=11, y=1)

image3 = Label(frame3, bg="#2B3467")
image3.place(x=11, y=22)

day_night_temp_label3 = Label(frame3, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label3.place(x=-4, y=55)

# fourth frame
frame4 = Frame(window, width=55, height=85, bg='#2B3467')
frame4.place(x=481, y=336)

day4 = Label(frame4, font="arial 14", bg="#2B3467", fg="#ffffff")
day4.place(x=11, y=1)

image4 = Label(frame4, bg="#2B3467")
image4.place(x=11, y=22)

day_night_temp_label4 = Label(frame4, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label4.place(x=-4, y=55)

# fifth frame
frame5 = Frame(window, width=55, height=85, bg='#2B3467')
frame5.place(x=581, y=336)

day5 = Label(frame5, font="arial 14", bg="#2B3467", fg="#ffffff")
day5.place(x=11, y=1)

image5 = Label(frame5, bg="#2B3467")
image5.place(x=11, y=22)

day_night_temp_label5 = Label(frame5, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label5.place(x=-4, y=55)

# sixth frame
frame6 = Frame(window, width=55, height=85, bg='#2B3467')
frame6.place(x=681, y=336)

day6 = Label(frame6, font="arial 14", bg="#2B3467", fg="#ffffff")
day6.place(x=11, y=1)

image6 = Label(frame6, bg="#2B3467")
image6.place(x=11, y=22)

day_night_temp_label6 = Label(frame6, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label6.place(x=-4, y=55)

# seventh frame
frame7 = Frame(window, width=55, height=85, bg='#2B3467')
frame7.place(x=781, y=336)

day7 = Label(frame7, font="arial 14", bg="#2B3467", fg="#ffffff")
day7.place(x=11, y=1)

image7 = Label(frame7, bg="#2B3467")
image7.place(x=11, y=22)

day_night_temp_label7 = Label(frame7, font="arial 10", bg="#2B3467", fg="#EB455F")
day_night_temp_label7.place(x=-4, y=55)

mainloop()
