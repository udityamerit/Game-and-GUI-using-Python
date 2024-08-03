import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox as tkmb
from PIL import ImageTk, Image 
from datetime import datetime
import requests
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        messagebox.showwarning("Input Error", "Please enter a city name")
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

    plot_type = plot_type_var.get()
    df1 = pd.read_csv('weather.csv')
    s = df1['Station.Location'].head(15)
    max_temp = df1['Data.Temperature.Max Temp'].head(15)
    min_temp = df1['Data.Temperature.Min Temp'].head(15)

    if plot_type == "Bar Plot":
        ax.bar(s, max_temp, label='Max Temp', color='green')
        ax.bar(s, min_temp, label='Min Temp', color='red', bottom=max_temp)
        ax.set_ylabel("Temperature")
        ax.set_xlabel("Location")
        ax.set_xticks(rotation=-75)
        ax.legend(loc='best')
    elif plot_type == "Pie Plot":
        ax.pie(max_temp, labels=s, autopct='%0.1f%%')
    elif plot_type == "Line Plot":
        ax.plot(s, max_temp, marker="o", color='green', label='Max Temp')
        ax.plot(s, min_temp, marker="o", color='red', label='Min Temp')
        ax.set_ylabel("Temperature")
        ax.set_xlabel("Location")
        ax.set_xticks(rotation=-75)
        ax.legend(loc='best')

    canvas.draw()

# Destroy the main window
def Close():
    root.destroy()

# Set up the GUI
root = tk.Tk()

# For main window
root.title("Weather Forecasting Dashboard")
root.geometry("820x820")
root.minsize(920,820)
root.maxsize(1100,1100)
img = tk.PhotoImage(file='white.png')
root.iconphoto(False, img)
set_background(root, 'OIG2.jpeg')  

# For second window
second_window = tk.Toplevel(root)
second_window.title("Weather Forecasting Dashboard")
second_window.geometry("820x820")
second_window.minsize(920,820)
second_window.maxsize(1120,1120)
img = tk.PhotoImage(file='white.png')
second_window.iconphoto(False, img)
set_background(second_window, 'OIG2.jpeg')
second_window.withdraw() 

switch_button = tk.Button(root,font=("Courier",12), text="Next Window", command=open_second_window, fg="purple", relief="groove", bg="#ff9633", borderwidth=5, pady=3)
switch_button.pack()

fig, ax = plt.subplots()

# Creating a frame of application to plot the graphs
frame = tk.Frame(second_window)

label = tk.Label(master=second_window, text="Graphical Representation")
label.config(font=("Courier",15), relief="raised", borderwidth=3, fg="purple", background='orange', pady=4)
label.pack()

canvas = FigureCanvasTkAgg(fig, master=second_window)
canvas.get_tk_widget().pack()
frame.pack()

# Dropdown menu for plot type selection
plot_type_var = tk.StringVar()
plot_type_var.set("Bar Plot")
plot_type_menu = ttk.Combobox(frame, textvariable=plot_type_var, values=["Bar Plot", "Pie Plot", "Line Plot"])
plot_type_menu.pack(pady=10)

tk.Button(frame, text="Plot Graph", fg="purple", relief="groove", borderwidth=5, command=plot, font=("Courier",15)).pack()

# Button to switch back to the main window
back_button = tk.Button(second_window, text="Back to Main Window", font=("Courier",15), command=back_to_root, fg="purple", relief="groove", borderwidth=5, pady=3)
back_button.pack()

city_label = tk.Label(root, text="Enter Name Of City/Country", font=("Robotomono",25,"bold"), foreground="green", bg="#D2F7F4")
city_label.pack(pady=19)

city_entry = tk.Entry(font=("Robotomono", 25), fg="blue", bg="#D2F7F4") 
city_entry.pack(pady=10)

weather_button = tk.Button(root,font=("Robotomono",19), text="⛅ Get Weather", command=show_weather, fg="green", relief="sunken", borderwidth=10)
weather_button.pack(pady=10)

weather_label = tk.Label(root, font=("Robotomono", 30), bg=None)
weather_label.pack(pady=10)

# Exit button
exit_button = tk.Button(root,font=("Robotomono",19), text="Exit", fg="red", borderwidth=9, relief="groove", command=Close) 
exit_button.pack()

root.mainloop()
