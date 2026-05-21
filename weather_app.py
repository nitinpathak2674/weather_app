import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "901b471c75a5e9d7e5e640d446368c6d"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result.config(
            text=f"""
City: {city_name}, {country}

Temperature: {temp}°C
Feels Like: {feels_like}°C
Humidity: {humidity}%

Weather: {weather.title()}
"""
        )

    except:
        messagebox.showerror("Error", "Something went wrong")

root = tk.Tk()
root.title("Weather App")
root.geometry("500x450")
root.config(bg="#1e1e2f")

title = tk.Label(
    root,
    text="Real-Time Weather App",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=20)

city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    justify="center"
)

city_entry.pack(pady=20)

search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=5,
    command=get_weather
)

search_btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="lightblue",
    justify="left"
)

result.pack(pady=30)

root.mainloop()