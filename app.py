"""Main application file."""

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from config import (
    MOISTURE_RANGE, TEMPERATURE_RANGE, PH_RANGE, 
    CONDUCTIVITY_RANGE, PHOSPHORUS_RANGE, KALIUM_RANGE
)
from styles import DASHBOARD_STYLES
from data_handler import fetch_data
from charts import create_chart
from components import (
    render_header, render_sidebar, 
    render_metrics, render_footer
)

# Streamlit Configuration
st.set_page_config(
    page_title="Smart Soil Monitor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply styles
st.markdown(DASHBOARD_STYLES, unsafe_allow_html=True)

# Auto-refresh every 30 seconds
st_autorefresh(interval=30000, limit=None, key="data_refresh")

def main():
    """Main application function."""
    # Render header
    render_header()

    # Render sidebar and get results
    results = render_sidebar(None)  # TODO: Implement callback if needed

    # Fetch and process data
    data = fetch_data(results)
    if data.empty:
        st.error("⚠️ No data available!")
        return

    # Render metrics
    render_metrics(data)

    # Charts Section
    st.subheader("📈 Sensor Readings Over Time")
    
    # First Row of Charts
    col1, col2 = st.columns(2)
    with col1:
        moisture_chart = create_chart(
            data, "created_at", "field1",
            "Soil Moisture",
            "Moisture (%)",
            "#00BCD4",
            MOISTURE_RANGE
        )
        st.plotly_chart(moisture_chart, use_container_width=True)

    with col2:
        temp_chart = create_chart(
            data, "created_at", "field2",
            "Temperature Variations",
            "Temperature (°C)",
            "#FF5722",
            TEMPERATURE_RANGE
        )
        st.plotly_chart(temp_chart, use_container_width=True)

    # Second Row of Charts
    col3, col4 = st.columns(2)
    with col3:
        ph_chart = create_chart(
            data, "created_at", "field3",
            "pH Level Changes",
            "pH Level",
            "#4CAF50",
            PH_RANGE
        )
        st.plotly_chart(ph_chart, use_container_width=True)

    with col4:
        conductivity_chart = create_chart(
            data, "created_at", "field4",
            "Soil Conductivity",
            "Conductivity (µS/cm)",
            "#FFC107",
            CONDUCTIVITY_RANGE
        )
        st.plotly_chart(conductivity_chart, use_container_width=True)

    # NPK Analysis Section
    st.subheader("🧪 NPK Analysis")
    npk_cols = st.columns(3)
    
    with npk_cols[0]:
        nitrogen_chart = create_chart(
            data, "created_at", "field5",
            "Nitrogen Levels",
            "Nitrogen (mg/L)",
            "#9C27B0"
        )
        st.plotly_chart(nitrogen_chart, use_container_width=True)

    with npk_cols[1]:
        phosphorus_chart = create_chart(
            data, "created_at", "field6",
            "Phosphorus Levels",
            "Phosphorus (mg/L)",
            "#E91E63",
            PHOSPHORUS_RANGE
        )
        st.plotly_chart(phosphorus_chart, use_container_width=True)

    with npk_cols[2]:
        kalium_chart = create_chart(
            data, "created_at", "field7",
            "Kalium Levels",
            "Kalium (mg/L)",
            "#3F51B5",
            KALIUM_RANGE
        )
        st.plotly_chart(kalium_chart, use_container_width=True)

    # Render footer
    render_footer()

if __name__ == "__main__":
    main()