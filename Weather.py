from win10toast import ToastNotifier
import requests
from bs4 import BeautifulSoup

html_form = requests.get("https://weather.com/en-IN/weather/today/l/bc29c35d3711bc60e38744cbcdb5c2b35a7c3b48295e37c20db874ca45adfcca").text

soup = BeautifulSoup(html_form, "lxml")

current_rain = str(soup.find_all("span", class_ = "Column--precip--3JCDO"))
print(current_rain)
current_temp = str(soup.find_all("span", class_ = "CurrentConditions--tempValue--MHmYY")) 

if "%" not in current_rain[156:158]:
    weather = f"Current temperature in Neharpar is {current_temp[92:94]}° and chance of rain is {current_rain[156:159]}"
else:
    weather = f"Current temperature in Neharpar is {current_temp[92:94]}° and chance of rain is {current_rain[156:158]}"
    
n = ToastNotifier()

n.show_toast("Weather", weather, duration = 10)



