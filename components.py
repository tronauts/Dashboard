"""UI components and layouts."""

import streamlit as st
from datetime import datetime

def render_header():
    """Render the dashboard header."""
    st.markdown("""
        <div class="dashboard-header">
            <h1>🌱 Smart Soil Monitoring System</h1>
            <p>Real-time soil quality monitoring dashboard</p>
        </div>
    """, unsafe_allow_html=True)

def render_sidebar(results_callback):
    """Render the sidebar with controls."""
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/soil.png", width=100)
        st.title("Dashboard Controls")
        results = st.slider("Data Points to Display:", 
                          min_value=100, 
                          max_value=1000, 
                          value=650,
                          step=50)
        st.button("🔄 Refresh Data")
        return results

def render_metrics(data):
    """Render metric cards in two rows."""
    st.subheader("📊 Current Readings")
    
    # First Row
    metrics_row1 = st.columns(4)
    first_row_metrics = [
        ("Soil Moisture 💧", f"{data['field1'].iloc[-1]:.1f}%", "60-80%"),
        ("Temperature 🌡️", f"{data['field2'].iloc[-1]:.1f}°C", "22-26°C"),
        ("pH Level 🧪", f"{data['field3'].iloc[-1]:.1f}", "6.0-7.0"),
        ("Conductivity ⚡", f"{data['field4'].iloc[-1]:.1f} µS/cm", "40-65 µS/cm")
    ]
    
    for col, (label, value, ideal) in zip(metrics_row1, first_row_metrics):
        with col:
            st.markdown(f"""
                <div class="metric-card">
                    <h3>{label}</h3>
                    <h2>{value}</h2>
                    <p>Ideal Range: {ideal}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # Second Row (NPK)
    metrics_row2 = st.columns(3)
    second_row_metrics = [
        ("Nitrogen 🌿", f"{data['field5'].iloc[-1]:.1f} mg/L", "200-300 mg/L"),
        ("Phosphorus 🍃", f"{data['field6'].iloc[-1]:.1f} mg/L", "190-400 mg/L"),
        ("Kalium 🌱", f"{data['field7'].iloc[-1]:.1f} mg/L", "190-400 mg/L")
    ]
    
    for col, (label, value, ideal) in zip(metrics_row2, second_row_metrics):
        with col:
            st.markdown(f"""
                <div class="metric-card">
                    <h3>{label}</h3>
                    <h2>{value}</h2>
                    <p>Ideal Range: {ideal}</p>
                </div>
            """, unsafe_allow_html=True)

def render_footer():
    """Render the dashboard footer."""
    st.markdown("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; background-color: var(--surface-color); border-radius: 10px;">
            <p>Last Updated: {}</p>
            <p>Smart Soil Monitoring System v2.0</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)