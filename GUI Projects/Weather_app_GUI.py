
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image 
import requests

def get_weather(city):
    api_key = "3f4f458fc6d5cb3440d24074d29f7e82" 

    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_desc = data['weather'][0]['description']
        
        weather_info = f"🌡Temperature: {temperature}°C\n\n 💧 Humidity: {humidity}%\n\n 🕣 Pressure: {pressure} hPa\n\n Description: {weather_desc.capitalize()}"
    else:
        weather_info = "City not found"
    
    return weather_info

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

def set_background(root, image_path):

    image = Image.open(image_path)
    
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

# Set up the GUI

root = tk.Tk()
root.title("Weather App")
root.geometry("720x720")
set_background(root, 'OIG2.jpeg')  

  
city_label = tk.Label(root, text="Enter City:",font=("Robotomono",25,"bold"),foreground="blue",bg="#D2F7F4")
city_label.pack()


city_entry = tk.Entry(font=("Robotomono", 25), fg="blue", bg="#D2F7F4") 
city_entry.pack()



weather_button = tk.Button(root,font=("Robotomono",15), text=" ⛅ Get Weather", command=show_weather)
weather_button.pack()

weather_label = tk.Label(root, font=("Robotomono", 30),bg=None)
weather_label.pack()

def Close():
    root.destroy()
    
exit_button = tk.Button(root,font=("Robotomono",19), text="Exit", command=Close) 

exit_button.pack()
root.mainloop()
