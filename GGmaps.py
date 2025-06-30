import customtkinter as ctk
from geopy.geocoders import Nominatim
import folium
import webbrowser
import os

# Appearance & theme
ctk.set_appearance_mode("light")  # Or "system", "dark"
ctk.set_default_color_theme("green")  # Try "green", "blue", or custom themes

# --- App Setup ---
app = ctk.CTk()
app.title("Map Search 🌍")
app.geometry("500x300")
app.resizable(False, False)

# --- Search Function ---
def search_place():
    place = entry.get()
    if not place.strip():
        return

    geolocator = Nominatim(user_agent="geo_ui_app")
    location = geolocator.geocode(place)

    if location:
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
        folium.Marker([location.latitude, location.longitude], popup=location.address).add_to(m)
        m.save("map.html")
        webbrowser.open('file://' + os.path.realpath("map.html"))

# --- UI Elements ---
title = ctk.CTkLabel(app, text="Search a Location", font=("Segoe UI", 18, "bold"))
title.pack(pady=25)

entry = ctk.CTkEntry(app, placeholder_text="e.g. London, Tokyo, Sahara Desert", width=350, height=40)
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Search", command=search_place, width=200, height=40)
button.pack(pady=20)

footer = ctk.CTkLabel(app, text="Powered by OpenStreetMap + Folium", font=("Segoe UI", 11))
footer.pack(side="bottom", pady=10)

app.mainloop()
