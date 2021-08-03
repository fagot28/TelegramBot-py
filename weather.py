from pyowm import OWM
from pyowm.utils.config import get_default_config

place = input(" Введите город/страну: ")

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = OWM('key', config_dict )

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

#print(w)

temp = w.temperature('celsius')["temp"]

print ( "В городе " + place + " сейчас " + w.detailed_status )
print ( "Температура сейчас в районе " + str(temp) + " градусов" )

if temp < 10:
	print ("Сейчас холодно, одевайся тепло")
elif temp < 20:
	print ("Сейчас очень холодно, одевайся потеплее!")
else:
	print ("На улице лето!")
