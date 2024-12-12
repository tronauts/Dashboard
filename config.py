"""Configuration settings for the dashboard."""

# ThingSpeak Configuration
CHANNEL_ID = "2572257"
READ_API_KEY = "KHO554NBRCHPVLGB"
BASE_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}"

# Chart Configurations
CHART_HEIGHT = 400
CHART_MARGINS = dict(l=20, r=20, t=40, b=20)

# Sensor Ranges
MOISTURE_RANGE = [60, 80]
TEMPERATURE_RANGE = [22, 26]
PH_RANGE = [0, 14]
CONDUCTIVITY_RANGE = [40, 65]
PHOSPHORUS_RANGE = [190, 400]
KALIUM_RANGE = [190, 400]