import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Weather: {response.text}")
    else:
        print(f"Error: {response.status_code}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()