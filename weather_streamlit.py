import requests
import streamlit as st

# Your API key
API_KEY = "8c7fa4bf9ed24b868fd3ccc16bdd8ec7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Streamlit UI
st.title("🌤️ Weather App")
city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if city:
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            st.subheader(f"Weather in {city.title()}")
            st.write(f"🌡 Temperature: {data['main']['temp']} °C")
            st.write(f"💧 Humidity: {data['main']['humidity']}%")
            st.write(f"🌬 Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"☁ Condition: {data['weather'][0]['description'].title()}")
        else:
            st.error("City not found ❌")
    else:
        st.warning("Please enter a city name.")
