import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image 

url="https://www.timeanddate.com/weather/india"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img=Image.open("C:/Users/HP/Desktop/w.JPG")
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

def getWeather():
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser")
    location = soup.find('div', class_="h1").text
    temperature = soup.find('div', class_="h2").text
    #WeatherPrediction = soup.find('p').text
    #print(WeatherPrediction)
    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)

    temperatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold",20), bg="white")
locationLabel.grid(row=0,sticky="N", padx=100)
temperatureLabel = Label(master, font=("Calibri bold",70), bg="white")
temperatureLabel.grid(row=1,sticky="W", padx=40)
Label(master, image=img,bg="white").grid(row=1, sticky="E")
#WeatherPredictionLabel = Label(master,font=("Calibri bold",15), bg="white")
#WeatherPredictionLabel.grid(row=2,sticky="W", padx=40)
getWeather()
master.mainloop()

