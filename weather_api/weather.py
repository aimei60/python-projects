import requests

def get_API():
    api_key = '28f1c6bca294e4c4e1722df05d6c41a0'
    city = input("Enter a city name: ")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_k = data['main']['temp']
        description = data['weather'][0]['description']
        temp_c = temp_k - 273.15
        print(f'Temperature: {temp_c:.2f} Celsius')
        print(f'Description: {description}')
    else:
        print("Error fetching weather data")
        
if __name__ == "__main__":
    get_API()