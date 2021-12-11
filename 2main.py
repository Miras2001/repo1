import requests
import datetime
from config import token_bot, owm_key
from pprint import pprint

def get_weather(city, owm_key):
    
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_key}&units=metric"
        )
        data = r.json()
        pprint(data)
        
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        feels = data["main"]["feels_like"]
        
        print(f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\n"
            f"Погода в городе:  {city}\nТемпература: {cur_weather}C°\n"
              f"Влажность: {humidity}%\nДавление: {pressure}mm.tt.rr\nВетер: {wind}m/s\n"
              f"Ощущается как: {feels}C°\n"
              f"Удачного дня!"
            
        )

        
    except Exception as ex:
        print(ex)
        print("Проверьте название города")
        
        
def main():
    city = input("Введитe город: ")
    get_weather(city, owm_key)
    
if __name__ == '__main__':
    main()
