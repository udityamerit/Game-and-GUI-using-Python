import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import ImageTk, Image
from datetime import datetime
import requests

def get_weather(city):
    api_key = "3f4f458fc6d5cb3440d24074d29f7e82"

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
        tkmb.showinfo(title='Input Error', message='Error! City or Country not found', icon='error')

def set_background(root, image_path):
    image = Image.open(image_path)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = ctk.CTkLabel(root, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

# Set up the GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather Forecasting Dashboard")
root.geometry("820x720")
root.minsize(820, 720)
root.maxsize(820, 720)

img = ctk.CTkImage(file='white.png')
root.iconphoto(False, img)

set_background(root, 'OIG2.jpeg')

city_label = ctk.CTkLabel(root, text="Enter Name Of City/Country", font=("Roboto", 25, "bold"), text_color="blue", bg_color="#D2F7F4")
city_label.pack(pady=19)

city_entry = ctk.CTkEntry(root, font=("Roboto", 25), text_color="blue", bg_color="#D2F7F4")
city_entry.pack(pady=10)

weather_button = ctk.CTkButton(root, font=("Roboto", 19), text=" ⛅ Get Weather", command=show_weather, text_color="green", fg_color="grey")
weather_button.pack(pady=10)

weather_label = ctk.CTkLabel(root, font=("Roboto", 30), text="")
weather_label.pack(pady=10)

def close_app():
    root.destroy()

exit_button = ctk.CTkButton(root, font=("Roboto", 19), text="Exit", command=close_app, text_color="red", fg_color="grey")
exit_button.pack(pady=10)

root.mainloop()
