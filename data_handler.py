"""Data fetching and processing functionality."""

import pandas as pd
import requests
import streamlit as st
from config import BASE_URL

def fetch_data(results):
    """Fetch and process data from ThingSpeak."""
    try:
        response = requests.get(BASE_URL, params={"results": results})
        response.raise_for_status()
        data = response.json()
        feeds = data.get("feeds", [])
        
        if feeds:
            df = pd.DataFrame(feeds)
            df["created_at"] = pd.to_datetime(df["created_at"]).dt.tz_convert("Asia/Jakarta")
            
            # Convert numeric columns
            numeric_fields = {
                "field1": "Soil Moisture",
                "field2": "Temperature",
                "field3": "pH",
                "field4": "Conductivity",
                "field5": "Nitrogen",
                "field6": "Phosphorus",
                "field7": "Kalium"
            }
            
            for field in numeric_fields:
                df[field] = pd.to_numeric(df[field], errors="coerce")
            
            # Resample data
            df.set_index("created_at", inplace=True)
            df_resampled = df.resample('10T').mean().reset_index()
            
            return df_resampled
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()