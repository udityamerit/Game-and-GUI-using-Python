import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as tkmb
from PIL import ImageTk, Image 
from datetime import datetime
import requests
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import numpy as np

# making the api key:
api_key = "3f4f458fc6d5cb3440d24074d29f7e82"
def get_weather(city):
     
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        sys = data['sys']
        clouds = data['clouds']
        
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_desc = data['weather'][0]['description']
        wind_speed = wind['speed']
        sunrise = datetime.fromtimestamp(sys['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(sys['sunset']).strftime('%H:%M:%S')
        cloudiness = clouds['all']
        
        weather_info = (
            f"🌡 Temperature: {temperature}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🕣 Pressure: {pressure} hPa\n"
            f"🌬 Wind Speed: {wind_speed} m/s\n"
            f"🌅 Sunrise: {sunrise}\n"
            f"🌇 Sunset: {sunset}\n"
            f"☁ Cloudiness: {cloudiness}%\n"
            f"🌤 Description: {weather_desc.capitalize()}"
        )
    else:
        weather_info = "City or Country not found"
    
    return weather_info

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        # messagebox.showwarning("Input Error", "Please enter a city name")

        tkmb.showinfo(title='Input Error', message='Error! City or Country not found', icon='error')

def set_background(root, image_path):

    image = Image.open(image_path)
    
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image,borderwidth=12,relief="sunken")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 


def open_second_window():
    root.withdraw()  # Hide the main window
    second_window.deiconify()  # Show the second window

def back_to_root():
    second_window.withdraw()  # Hide the second window
    root.deiconify()  # Show the main window

def plot():
    ax.clear()
    # x = np.random.randint(0,10,10)
    # y = np.random.randint(0,10,10)
    

    nRowsRead = 1000 # specify 'None' if want to read whole file
    df1 = pd.read_csv('weather.csv')
    s = df1['Station.Location'].head(10)
    x = df1['Data.Temperature.Max Temp'].head(10)
    y = df1['Data.Temperature.Min Temp'].head(10)
    plt.pie(x,labels=s,autopct='%0.1f%%')

    # plt.pie(y,labels=s,autopct='%0.1f%%')
    # plt.colorbar()
    canvas.draw()

# Destroy the main window
def Close():
    root.destroy()

# def Close1():
#     second_window.destroy()
    


# Set up the GUI
root = tk.Tk()


#  For main window
root.title("Weather Forcasting Dashboard")
root.geometry("820x820")
root.minsize(920,820)
root.maxsize(1020,1020)
img = tk.PhotoImage(file='white.png')
root.iconphoto(False, img)
set_background(root, 'OIG2.jpeg')  

#  For second window
second_window = tk.Toplevel(root)
second_window.title("Weather Forcasting Dashboard")
second_window.geometry("820x820")
second_window.minsize(920,820)
second_window.maxsize(1020,1020)
img = tk.PhotoImage(file='white.png')
second_window.iconphoto(False, img)
set_background(second_window, 'OIG2.jpeg')
second_window.withdraw() 


switch_button = tk.Button(root,font=("Courier",12), text=" Next Window", command=open_second_window,fg="purple",relief="groove",bg="#ff9633",borderwidth=5,pady=3)
switch_button.pack()

fig, ax = plt.subplots()


# creating a frame of application to plot the graphs

frame = tk.Frame(second_window)
label =tk.Label(master=second_window,text="Graphs")
label.config(font=("Courier",32),relief="raised",borderwidth=5,fg="purple",background='orange')
label.pack()
canvas = FigureCanvasTkAgg(fig, master=second_window)
canvas.get_tk_widget().pack()
frame.pack()

tk.Button(frame, text="Plot Graph",fg="purple",relief="groove",borderwidth=5, command=plot).pack()


# Button to switch back to the main window
back_button = tk.Button(second_window, text="Back to Main Window",font=("Courier",12), command=back_to_root,fg="purple",relief="groove",borderwidth=5,pady=3)
back_button.pack()

city_label = tk.Label(root, text="Enter Name Of City/Country",font=("Robotomono",25,"bold"),foreground="green",bg="#D2F7F4")
city_label.pack(pady=19)

city_entry = tk.Entry(font=("Robotomono", 25), fg="blue", bg="#D2F7F4") 
city_entry.pack(pady=10)

weather_button = tk.Button(root,font=("Robotomono",19), text=" ⛅ Get Weather", command=show_weather,fg="green",relief="sunken",borderwidth=10)
weather_button.pack(pady=10)

weather_label = tk.Label(root, font=("Robotomono", 30),bg=None)
weather_label.pack(pady=10)

# exit buttons
exit_button = tk.Button(root,font=("Robotomono",19), text="Exit",fg="red",borderwidth=9,relief="groove", command=Close) 

# exit_button1 = tk.Button(second_window,font=("Robotomono",19), text="Exit",fg="red",borderwidth=9,relief="sunken", command=Close1) 

exit_button.pack()

# exit_button1.pack()

root.mainloop()
