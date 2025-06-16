
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# --- SETTINGS ---
API_KEY = 'YOUR_API_KEY'  
CITY = 'London'
UNITS = 'metric'  # Use 'imperial' for Fahrenheit

# --- FETCH WEATHER FORECAST DATA ---
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'
response = requests.get(url)
data = response.json()

# --- PARSE DATA ---
dates = []
temps = []

for entry in data['list']:
    dt = datetime.datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    dates.append(dt)
    temps.append(temp)

sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
plt.plot(dates, temps, marker='o', linestyle='-', color='teal')
plt.title(f'5-Day Weather Forecast for {CITY}', fontsize=16)
plt.xlabel('Date & Time')
plt.ylabel(f'Temperature ({ "°C" if UNITS=="metric" else "°F" })')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
