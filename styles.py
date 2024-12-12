"""CSS styles for the dashboard."""

DASHBOARD_STYLES = """
<style>
    /* Main Theme Colors */
    :root {
        --primary-color: #2E7D32;
        --secondary-color: #1B5E20;
        --background-color: #121212;
        --surface-color: #1E1E1E;
        --text-color: #E0E0E0;
        --accent-color: #4CAF50;
    }

    /* Global Styles */
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
    }

    /* Header Styling */
    .dashboard-header {
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Metric Cards */
    .metric-card {
        background: var(--surface-color);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid var(--accent-color);
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Chart Container */
    .chart-container {
        background: var(--surface-color);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: var(--surface-color);
    }

    /* Custom Metric Styling */
    .stMetric {
        background-color: var(--surface-color) !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
    }

    /* Text Elements */
    h1, h2, h3 {
        color: var(--text-color) !important;
        font-weight: 600 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: var(--primary-color) !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: var(--secondary-color) !important;
        transform: translateY(-2px) !important;
    }
</style>
"""