import requests

api_key = '2ef52a9fcbe65cda08f19671a9ac03a6'

user_input = input("Enter city: ")

try:
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

    weather_data = response.json()

    if weather_data['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']

        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºC")
        print(f"The humidity in {user_input} is: {humidity}%")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
except Exception as err:
    print(f"An error occurred: {err}")
