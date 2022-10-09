import requests
import creads

location=input('Enter city name : ')
main_link="http://api.weatherstack.com/current?access_key="+creads.api+"&query="+location
data=requests.get(main_link).json()

temp=(data['current']['temperature'])
weth_des= data['current']['weather_descriptions']
humid= data['current']['humidity']
pres= data['current']['pressure']
wind_speed=data['current']['wind_speed']
uv=data['current']['uv_index']
visiblity=data['current']['visibility']
dayornight=data['current']['is_day']

print("--------------------------------------------------")
print(f'Temperature of {location} is {temp} degree c')
print("--------------------------------------------------")
print(f"Weather is {weth_des}")
print("--------------------------------------------------")
print(f"Humidity = {humid}")
print("--------------------------------------------------")
print(f"Pressure = {pres} atm")
print("--------------------------------------------------")
print(f"Wind Speed = {wind_speed} kmps ")
print("--------------------------------------------------")
print(f"UV Index = {uv}")
print("--------------------------------------------------")
print(f"Visiblity = {visiblity}")
print("--------------------------------------------------")
if dayornight=="yes":
    print ("Day")
else:
    print("Night")
print("---------------------------------------------------")
