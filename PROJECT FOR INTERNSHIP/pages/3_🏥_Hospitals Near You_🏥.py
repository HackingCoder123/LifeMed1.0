import streamlit as st
from geopy.geocoders import Nominatim
import requests
import folium
from streamlit_folium import st_folium

# Streamlit app title
st.title("Find Hospitals Near You")

# Create a one-column layout
col1 = st.container()

# Get user location in the first column
with col1:
    user_location = st.text_input("Enter your location (e.g., city, address):")

    if user_location:
        # Initialize the geocoder
        geolocator = Nominatim(user_agent="hospital_finder")

        # Geocode user's location
        location = geolocator.geocode(user_location)
        if location:
            st.write(f"Your Location: {location.address}")
            user_lat, user_lon = location.latitude, location.longitude

            # Create a Google Maps link with the user's location
            google_maps_url = f"https://www.google.com/maps?q={user_lat},{user_lon}"
            st.markdown(f"Open this link in Google Maps to view your location: [Google Maps]({google_maps_url})")

            # Create a Folium map centered on the user's location
           
            m = folium.Map(location=[user_lat, user_lon], zoom_start=50)

            # Example marker with a pop-up
            folium.Marker(
                location=[user_lat, user_lon],
                popup='Your Location'
                ).add_to(m)


            # Find hospitals near the user's location using OpenStreetMap data
            overpass_url = "https://overpass-api.de/api/interpreter"
            query = f"""
                [out:json];
                node["amenity"="hospital"](around:5000,{user_lat},{user_lon});
                out;
            """
            response = requests.post(overpass_url, data=query)

            if response.status_code == 200:
                data = response.json()
                hospitals = data.get("elements", [])

                st.write(f"Found {len(hospitals)} hospitals near you:")

                for hospital in hospitals:
                    name = hospital.get("tags", {}).get("name", "Unknown Hospital")
                    st.write(f"- {name}")

                # Add the Folium map to Streamlit using st_folium
                st_folium(m, width=2000, height=1000)  # Adjust width and height as needed
            else:
                st.error("Error fetching hospital data.")
        else:
            st.error("Location not found. Please try a different location")
