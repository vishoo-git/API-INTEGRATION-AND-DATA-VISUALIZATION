import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

# Step 2: Extract relevant weather information
def extract_weather_info(data):
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return city_name, temperature, humidity, wind_speed

# Step 3: Visualize the data
def visualize_weather(temperature, humidity, wind_speed):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [temperature, humidity, wind_speed]

    # Create a bar plot using Seaborn
    sns.set(style="whitegrid")
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['#FF6347', '#4682B4', '#32CD32'])
    
    ax.set_ylabel('Values')
    ax.set_title('Weather Data')

    plt.show()

# Main function to get data and visualize
def main():
    api_key = 'your_openweathermap_api_key'  # Replace with your API key
    city = 'London'  # Replace with the city of your choice

    # Fetch and extract data
    weather_data = fetch_weather_data(api_key, city)
    city_name, temperature, humidity, wind_speed = extract_weather_info(weather_data)

    print(f"Weather data for {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

    # Visualize the data
    visualize_weather(temperature, humidity, wind_speed)

# Run the main function
if __name__ == '__main__':
    main()
